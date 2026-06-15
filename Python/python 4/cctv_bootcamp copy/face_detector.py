import os
import json
import dlib
from PIL import Image

# =========================
# KONFIGURASI
# =========================
SOURCE_FOLDER = "resource"          # folder gambar asli
FIXED_FOLDER = "resource_fixed"     # folder hasil normalisasi
OUTPUT_FILE = "face_encodings.jsonl"

SHAPE_PREDICTOR = "models/shape_predictor_68_face_landmarks.dat"
FACE_MODEL = "models/dlib_face_recognition_resnet_model_v1.dat"

os.makedirs(FIXED_FOLDER, exist_ok=True)

# =========================
# LOAD MODEL DLIB
# =========================
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(SHAPE_PREDICTOR)
face_rec_model = dlib.face_recognition_model_v1(FACE_MODEL)

# =========================
# STEP 1: NORMALISASI GAMBAR
# =========================
print("🔄 Normalisasi gambar (RGB 8-bit)...")

fixed_images = []

for filename in os.listdir(SOURCE_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        src_path = os.path.join(SOURCE_FOLDER, filename)
        dst_path = os.path.join(FIXED_FOLDER, filename)

        try:
            img = Image.open(src_path)
            img = img.convert("RGB")  # PAKSA RGB 8-bit
            img.save(dst_path, format="JPEG", quality=95, subsampling=0)
            fixed_images.append(filename)
            print(f"✔ Fixed: {filename}")
        except Exception as e:
            print(f"❌ Gagal normalisasi {filename}: {e}")

# =========================
# STEP 2: FACE ENCODING
# =========================
print("\n🧠 Proses face encoding...")
encodings = []

for filename in fixed_images:
    name = os.path.splitext(filename)[0]
    image_path = os.path.join(FIXED_FOLDER, filename)

    try:
        image = dlib.load_rgb_image(image_path)
        faces = detector(image, 1)
    except Exception as e:
        print(f"❌ Error load/detect {filename}: {e}")
        continue

    if len(faces) == 0:
        print(f"⚠️ Tidak ada wajah: {filename}")
        continue

    for rect in faces:
        shape = sp(image, rect)
        encoding = face_rec_model.compute_face_descriptor(image, shape)

        encodings.append({
            "name": name,
            "encoding": list(encoding)
        })
        print(f"✅ Encoding sukses: {filename}")
        break  # ambil 1 wajah saja

# =========================
# STEP 3: SIMPAN KE JSONL
# =========================
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for item in encodings:
        f.write(json.dumps(item) + "\n")

print(f"\n🎉 SELESAI")
print(f"Total wajah berhasil diencoding: {len(encodings)}")
print(f"Output file: {OUTPUT_FILE}")
