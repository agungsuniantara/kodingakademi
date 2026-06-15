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
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# Define folders for data storage
jsonl_folder = "jsonl_data"
xlsx_folder = "xlsx_data"
screenshots_folder = "screenshots"

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
                'timestamp': data.get('timestamp', 0),
                'screenshot': data.get('screenshot', None)
            })
    return detections

def is_violation(cls):
    """Check if class is a violation."""
    return cls.lower().startswith('no-')

def classify_apd(cls):
    """Classify APD class as violation or compliance."""
    if is_violation(cls):
        return 'pelanggaran', cls
    else:
        return 'kepatuhan', cls

def save_screenshot(frame, timestamp, folder):
    """Save screenshot to file with compression."""
    os.makedirs(folder, exist_ok=True)
    filename = f"screenshot_{timestamp}.jpg"
    filepath = os.path.join(folder, filename)
    # Compress image with JPEG quality 70 to reduce file size
    cv2.imwrite(filepath, frame, [cv2.IMWRITE_JPEG_QUALITY, 20])
    return filepath

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

                # Get annotated frame
                annotated_frame = results[0].plot()

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

                    timestamp = time.time()
                    screenshot_path = None
                    if any(is_violation(cls) for cls in classes):
                        screenshot_path = save_screenshot(annotated_frame, timestamp, screenshots_folder)

                    record = {
                        "classes": classes,
                        "person_encodings": person_encodings,
                        "timestamp": timestamp,
                        "screenshot": screenshot_path
                    }
                    save_detection_jsonl(detection_file, record)

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
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        detection_file = os.path.join(jsonl_folder, f"{current_date}.jsonl")
        detections = load_detection_data(detection_file)

        if detections:
            # Collect all classes from detections
            all_classes = []
            violation_logs = []
            for detection in detections:
                for cls in detection['classes']:
                    all_classes.append(cls)
                if detection['screenshot']:
                    dt = datetime.datetime.fromtimestamp(detection['timestamp'])
                    waktu = dt.strftime("%Y-%m-%d %H:%M")
                    for cls in detection['classes']:
                        if is_violation(cls):
                            violation_logs.append({
                                'waktu': waktu,
                                'kondisi': cls,
                                'dokumentasi': detection['screenshot']
                            })

            # Summary: count per subjek and apd
            summary_counts = defaultdict(int)
            for cls in all_classes:
                subjek, apd = classify_apd(cls)
                summary_counts[(subjek, apd)] += 1

            summary_data = []
            no = 1
            for (subjek, apd), count in summary_counts.items():
                summary_data.append({
                    'no': no,
                    'subjek': subjek,
                    'apd': apd,
                    'counting': count
                })
                no += 1

            summary_df = pd.DataFrame(summary_data)

            # Log pelanggaran
            log_data = []
            no = 1
            for log in violation_logs:
                log_data.append({
                    'no': no,
                    'waktu': log['waktu'],
                    'kondisi': log['kondisi'],
                    'dokumentasi': log['dokumentasi']
                })
                no += 1

            log_df = pd.DataFrame(log_data)

            os.makedirs(xlsx_folder, exist_ok=True)
            excel_file = os.path.join(xlsx_folder, f"{current_date}.xlsx")
            with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
                log_df.to_excel(writer, sheet_name='Log Pelanggaran', index=False)

            # Load workbook to insert images
            wb = load_workbook(excel_file)
            ws = wb['Log Pelanggaran']
            for row in range(2, len(log_data) + 2):  # Start from row 2
                img_path = ws[f'D{row}'].value
                if img_path and os.path.exists(img_path):
                    img = Image(img_path)
                    img.width = 100  # Resize image
                    img.height = 100
                    ws.add_image(img, f'D{row}')
                    ws[f'D{row}'] = ''  # Clear text, keep image

            wb.save(excel_file)

            st.success(f"Detection results exported to {excel_file}")
        else:
            st.warning("No detection data to export.")
    except Exception as e:
        st.error(f"Error exporting to Excel: {str(e)}")

# Footer
st.markdown("---")
st.markdown("**APD Detection App** - Powered by YOLOv8 and Streamlit")
