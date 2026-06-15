from ultralytics import YOLO
import os
import numpy as np
import yaml

model = YOLO("models/best.pt")

CONF_THRESHOLD = 0.25

image_dir = "datasets_baru/train/images"
label_dir = "datasets_baru/train/labels"
os.makedirs(label_dir, exist_ok=True)

for img_file in os.listdir(image_dir):
    if img_file.endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(image_dir, img_file)
        
        results = model(img_path, conf=CONF_THRESHOLD, verbose=False)

        boxes = results[0].boxes.xywhn.cpu().numpy()
        classes = results[0].boxes.cls.cpu().numpy().astype(int)

        label_path = os.path.join(label_dir, img_file.rsplit(".", 1)[0] + ".txt")
        with open(label_path, "w") as f:
            for i in range(len(boxes)):
                cls = classes[i]
                box = boxes[i]
                x, y, w, h = box
                f.write(f"{cls} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")

class_names = model.names

classes_txt_path = "datasets_baru/train/labels/classes.txt"
with open(classes_txt_path, "w") as f:
    for name in class_names.values():
        f.write(f"{name}\n")

print(f"\nAuto-labeling selesai (menyimpan semua deteksi dengan confidence > {CONF_THRESHOLD})")

yaml_path = 'data.yaml'
try:
    with open(yaml_path, 'r') as f:
        data_yaml = yaml.safe_load(f)

    existing_names = data_yaml.get('names', [])
    if existing_names is None:
        existing_names = []
    for model_name in class_names.values():
        if model_name not in existing_names:
            existing_names.append(model_name)

    data_yaml['nc'] = len(existing_names)
    data_yaml['names'] = existing_names

    with open(yaml_path, 'w') as f:
        yaml.dump(data_yaml, f, sort_keys=False)

    print(f"File {yaml_path} telah diperbarui dengan {len(existing_names)} kelas.")

except FileNotFoundError:
    print(f"Error: File {yaml_path} tidak ditemukan. Tidak dapat memperbarui.")
except Exception as e:
    print(f"Terjadi error saat memperbarui {yaml_path}: {e}")
