# app.py
import streamlit as st
import cv2
import json
import time
from ultralytics import YOLO
import dlib
import numpy as np

def save_detection_jsonl(filepath, record):
    """Append a single detection record (dict) as a JSON line."""
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def run_detection_in_ui(placeholder):
    model_path = 'runs/detect/train/weights/best.pt'
    video_source = 0

    conf_threshold = 0.1

    try:
        model = YOLO(model_path)
        sp = dlib.shape_predictor("model_jadi/shape_predictor_68_face_landmarks.dat")
        face_rec_model = dlib.face_recognition_model_v1("model_jadi/dlib_face_recognition_resnet_model_v1.dat")
    except Exception as e:
        print(f"Error saat memuat model: {e}")
        return

    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print(f"Error: Tidak dapat membuka kamera (sumber: {video_source})")
        return

    try:
        while True:
            if st.session_state.get('should_stop', False):
                break

            success, frame = cap.read()
            if not success:
                placeholder.error("Gagal membaca frame dari kamera.")
                break

            results = model(frame, conf=conf_threshold, verbose=False)

            boxes = results[0].boxes
            names = model.names

            person_detected = any(names[int(box.cls[0])].lower() == "orang" for box in boxes)

            if person_detected:
                classes = []
                person_encodings = []
                for box in boxes:
                    cls_id = int(box.cls[0])
                    class_name = names[cls_id]

                    if class_name.lower() != "orang":
                        classes.append(class_name)
                    else:
                        x1, y1, x2, y2 = box.xyxy[0].tolist()
                        face_rect = dlib.rectangle(int(x1), int(y1), int(x2), int(y2))
                        shape = sp(frame, face_rect)
                        encoding = face_rec_model.compute_face_descriptor(frame, shape)
                        person_encodings.append(list(encoding))

                record = {
                    "classes": classes,
                    "person_encodings": person_encodings
                }
                save_detection_jsonl("detection_output.jsonl", record)

            annotated_frame = results[0].plot()
            annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            placeholder.image(annotated_frame_rgb, caption="Deteksi APD Real-time")

            time.sleep(0.05)  # Mengontrol frame rate
    except Exception as e:
        placeholder.error(f"Error dalam deteksi: {e}")
    finally:
        cap.release()
        print("Kamera dilepaskan.")

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Deteksi APD - Streamlit Launcher", layout="wide")

st.title("Deteksi APD (YOLO + dlib) — Streamlit")
st.write("Interface untuk menjalankan dan menghentikan deteksi APD real-time yang ditampilkan langsung di Streamlit.")

col1, col2 = st.columns(2)

with col1:
    start_btn = st.button("Jalankan Deteksi", key="start", disabled=st.session_state.get('running', False))

with col2:
    stop_btn = st.button("Hentikan Deteksi", key="stop", disabled=not st.session_state.get('running', False))

if start_btn:
    st.session_state['running'] = True
    st.session_state['should_stop'] = False
    st.rerun()

if stop_btn:
    st.session_state['should_stop'] = True
    st.session_state['running'] = False
    st.success("Deteksi dihentikan.")
    st.rerun()

if st.session_state.get('running', False):
    placeholder = st.empty()
    run_detection_in_ui(placeholder)
