import cv2
import json
import time
from ultralytics import YOLO
import dlib
import numpy as np

def save_detection_jsonl(filepath, record):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
        
model_path = 'models/best.pt'
video_source = 0

conf_threshold = 0.25

model = YOLO(model_path)
sp = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")

cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print(f"Error: Tidak dapat membuka kamera (sumber: {video_source})")

while True:
    success, frame = cap.read()
    if not success:
        print("Gagal membaca frame dari kamera.")
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
        save_detection_jsonl("detection_output.jsonl", record)

    annotated_frame = results[0].plot()

    cv2.imshow("Deteksi APD Real-time", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("Program dihentikan.")
