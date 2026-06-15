import dlib
import cv2
import os
import json

# Load models
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("model_jadi/shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("model_jadi/dlib_face_recognition_resnet_model_v1.dat")

def extract_face_encodings(folder_path):
    encodings = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            name = os.path.splitext(filename)[0]  # Get name without extension
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            if image is None:
                print(f"Gagal membaca gambar: {filename}")
                continue

            # Convert to grayscale for detection
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            for rect in faces:
                shape = sp(image, rect)
                encoding = face_rec_model.compute_face_descriptor(image, shape)
                encodings.append({
                    "name": name,
                    "encoding": list(encoding)
                })
                break  # Only take first face

    return encodings

if __name__ == "__main__":
    folder_path = "foto"
    encodings = extract_face_encodings(folder_path)

    with open("face_encodings.jsonl", "w", encoding="utf-8") as f:
        for encoding in encodings:
            f.write(json.dumps(encoding, ensure_ascii=False) + "\n")

    print("Face encodings saved to face_encodings.jsonl")
