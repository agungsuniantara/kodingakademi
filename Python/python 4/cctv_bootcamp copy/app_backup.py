import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import numpy as np
import time
from PIL import Image
import dlib
import json
import pandas as pd
from collections import defaultdict
import os
import datetime

# Define folders for data storage
jsonl_folder = "jsonl_data"
xlsx_folder = "xlsx_data"

def save_detection_jsonl(filepath, record):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def load_known_encodings(file_path):
    """Load known face encodings from JSONL file."""
    encodings = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            encodings.append({
                'name': data['name'],
                'encoding': np.array(data['encoding'])
            })
    return encodings

def load_detection_data(file_path):
    """Load detection data from JSONL file."""
    detections = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            detections.append({
                'classes': data.get('classes', []),
                'person_encodings': [np.array(enc) for enc in data.get('person_encodings', [])],
                'timestamp': data.get('timestamp', 0)
            })
    return detections

def find_best_match(person_encoding, known_encodings, threshold=0.6):
    """Find the best matching known face for a person encoding."""
    best_match = None
    best_similarity = -1

    person_norm = person_encoding / np.linalg.norm(person_encoding)

    for known in known_encodings:
        known_norm = known['encoding'] / np.linalg.norm(known['encoding'])
        similarity = np.dot(person_norm, known_norm)

        if similarity > best_similarity:
            best_similarity = similarity
            best_match = known['name']

    if best_similarity >= threshold:
        return best_match, best_similarity
    else:
        return "Unknown", best_similarity

st.title("Real-time APD Detection")
st.write("Aplikasi deteksi APD menggunakan YOLOv8")

with st.sidebar:
    st.header("Settings")
    model_path = st.selectbox(
        "Model Path",
        ['models/best.pt', 'runs/detect/train5/weights/best.pt', 'runs/detect/train4/weights/best.pt'],
        index=1
    )
    conf_threshold = st.slider("Confidence Threshold", 0.1, 1.0, 0.25)
    start_detection = st.button("Start Detection")
    stop_detection = st.button("Stop Detection")

if start_detection:
    st.session_state["detecting"] = True

if stop_detection:
    st.session_state["detecting"] = False

placeholder = st.empty()

if st.session_state.get("detecting", False):
    try:
        with st.spinner("Loading model..."):
            model = YOLO(model_path)
            sp = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
            face_rec_model = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")

        st.success("Model loaded successfully!")

        # Generate date-based filename for detection output
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        os.makedirs(jsonl_folder, exist_ok=True)
        detection_file = os.path.join(jsonl_folder, f"{current_date}.jsonl")

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("Cannot access webcam. Please check if webcam is available.")
        else:
            while st.session_state["detecting"]:
                current_time = datetime.datetime.now().time()
                if current_time >= datetime.time(23, 0):
                    st.session_state["detecting"] = False
                    st.info("Detection stopped automatically at 23:00.")
                    break

                ret, frame = cap.read()
                if not ret:
                    st.error("Failed to read frame from webcam.")
                    break

                results = model(frame, conf=conf_threshold, verbose=False)
                
                boxes = results[0].boxes
                names = model.names
                
                person_detected = any(names[int(box.cls[0])].lower() == "person" for box in boxes)
                
                if person_detected:
                    classes = []
                    person_encodings = []
                    for box in boxes:
                        cls_id = int(box.cls[0])
                        class_name = names[cls_id]

                        if class_name.lower() != "person":
                            classes.append(class_name)
                        else:
                            x1, y1, x2, y2 = box.xyxy[0].tolist()
                            face_rect = dlib.rectangle(int(x1), int(y1), int(x2), int(y2))
                            shape = sp(frame, face_rect)
                            encoding = face_rec_model.compute_face_descriptor(frame, shape)
                            person_encodings.append(list(encoding))

                    record = {
                        "classes": classes,
                        "person_encodings": person_encodings,
                        "timestamp": time.time()
                    }
                    save_detection_jsonl(detection_file, record)

                # Get annotated frame
                annotated_frame = results[0].plot()

                # Convert BGR to RGB for Streamlit
                rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

                # Display frame
                placeholder.image(rgb_frame, channels="RGB", use_container_width=True)

                # Small delay to prevent overwhelming the interface
                time.sleep(0.1)

            cap.release()
            st.info("Detection stopped.")
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if stop_detection:
    # Export to Excel
    try:
        known_encodings = load_known_encodings('face_encodings.jsonl')
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        detection_file = os.path.join(jsonl_folder, f"{current_date}.jsonl")
        detections = load_detection_data(detection_file)
        
        if detections:
            all_combined_results = []
            for detection in detections:
                combined_results = []
                for i, person_encoding in enumerate(detection['person_encodings']):
                    match_name, similarity = find_best_match(person_encoding, known_encodings)
                    combined_results.append({
                        'person_id': i + 1,
                        'matched_name': match_name,
                        'similarity': similarity,
                        'classes': detection['classes'], 
                        'timestamp': detection['timestamp']
                    })
                all_combined_results.extend(combined_results)
            
            matched_person_data = {}
            for result in all_combined_results:
                name = result['matched_name']
                if name != "Unknown":
                    if name not in matched_person_data:
                        matched_person_data[name] = {'classes': set(), 'timestamps': [], 'similarities': []}
                    matched_person_data[name]['classes'].update(result['classes'])
                    matched_person_data[name]['timestamps'].append(result['timestamp'])

            matched_person_list = [{'Name': name, 'Detected Classes': list(data['classes'])} for name, data in matched_person_data.items()]
            matched_person_df = pd.DataFrame(matched_person_list)

            class_totals = defaultdict(int)
            for name, data in matched_person_data.items():
                for cls in data['classes']:
                    class_totals[cls] += 1

            count_df = pd.DataFrame(list(class_totals.items()), columns=['Class', 'Total Persons Detected'])

            os.makedirs(xlsx_folder, exist_ok=True)
            excel_file = os.path.join(xlsx_folder, f"{current_date}.xlsx")
            with pd.ExcelWriter(excel_file) as writer:
                matched_person_df.to_excel(writer, sheet_name='Matched Persons', index=False)
                count_df.to_excel(writer, sheet_name='Class Counts', index=False)
            
            st.success(f"Detection results exported to {excel_file}")
        else:
            st.warning("No detection data to export.")
    except Exception as e:
        st.error(f"Error exporting to Excel: {str(e)}")

# Footer
st.markdown("---")
st.markdown("**APD Detection App** - Powered by YOLOv8 and Streamlit")
