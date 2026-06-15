from ultralytics import YOLO
import os
import numpy as np
import yaml

# --- PENGATURAN ---
# Model yang digunakan untuk melakukan deteksi awal
model = YOLO("model_jadi/best.pt")
# Tingkat kepercayaan minimum untuk menyimpan sebuah deteksi
CONF_THRESHOLD = 0.25
# --- SELESAI PENGATURAN ---

image_dir = "datasets/data_kustom/train/images"
label_dir = "datasets/data_kustom/train/labels"
os.makedirs(label_dir, exist_ok=True)

print(f"Memulai auto-labeling pada gambar di '{image_dir}'...")

for img_file in os.listdir(image_dir):
    if img_file.endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(image_dir, img_file)
        
        # Lakukan deteksi dengan confidence threshold
        results = model(img_path, conf=CONF_THRESHOLD, verbose=False)

        # Ambil box dan class yang sudah difilter oleh model
        boxes = results[0].boxes.xywhn.cpu().numpy()
        classes = results[0].boxes.cls.cpu().numpy().astype(int)

        # Buat atau timpa file label
        label_path = os.path.join(label_dir, img_file.rsplit(".", 1)[0] + ".txt")
        with open(label_path, "w") as f:
            # Tulis setiap deteksi ke dalam file
            for i in range(len(boxes)):
                cls = classes[i]
                box = boxes[i]
                x, y, w, h = box
                f.write(f"{cls} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")

# Dapatkan nama kelas dari model
class_names = model.names

print(f"\nAuto-labeling selesai (menyimpan semua deteksi dengan confidence > {CONF_THRESHOLD})")

# --- Perbarui file data_kustom.yaml ---
yaml_path = 'data/data_kustom.yaml'
try:
    with open(yaml_path, 'r') as f:
        # Menggunakan safe_load untuk keamanan
        data_yaml = yaml.safe_load(f)

    # Jika ada nama kelas dari model yang belum ada, tambahkan
    existing_names = data_yaml.get('names', [])
    if existing_names is None:
        existing_names = []
    for model_name in class_names.values():
        if model_name not in existing_names:
            existing_names.append(model_name)

    # Perbarui nilai nc dan names
    data_yaml['nc'] = len(existing_names)
    data_yaml['names'] = existing_names

    # Tulis kembali ke file yaml
    with open(yaml_path, 'w') as f:
        yaml.dump(data_yaml, f, sort_keys=False)

    print(f"File {yaml_path} telah diperbarui dengan {len(existing_names)} kelas.")

except FileNotFoundError:
    print(f"Error: File {yaml_path} tidak ditemukan. Tidak dapat memperbarui.")
except Exception as e:
    print(f"Terjadi error saat memperbarui {yaml_path}: {e}")
