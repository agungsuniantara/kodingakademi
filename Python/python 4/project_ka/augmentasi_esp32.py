import cv2
import numpy as np
import os
import glob

def proses_gambar_esp32(input_path, output_path):
    """
    Fungsi untuk memanipulasi gambar resolusi tinggi agar menyerupai 
    hasil tangkapan kamera modul ESP32 (misal OV2640).
    """
    # 1. Membaca gambar
    img = cv2.imread(input_path)
    if img is None:
        print(f"  -> Gagal membaca: {input_path}")
        return

    # 2. Resize ke standar streaming ESP32 (QVGA 320x240)
    img_resized = cv2.resize(img, (320, 240))

    # 3. Kurangi Saturasi & Kontras (Mensimulasikan sensor OV2640 yang 'washed-out')
    img_hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV).astype("float32")
    img_hsv[:, :, 1] = img_hsv[:, :, 1] * 0.8  # Kurangi saturasi warna 20%
    img_hsv[:, :, 2] = img_hsv[:, :, 2] * 0.9  # Kurangi kecerahan 10%
    img_hsv = np.clip(img_hsv, 0, 255)
    img_color = cv2.cvtColor(img_hsv.astype("uint8"), cv2.COLOR_HSV2BGR)

    # 4. Efek Blur Ringan (Mensimulasikan lensa plastik bawaan pabrik)
    img_blurred = cv2.GaussianBlur(img_color, (3, 3), 0)

    # 5. Tambahkan Noise Sensor (Variansi diatur agar bentuk objek tetap utuh)
    row, col, ch = img_blurred.shape
    mean = 0
    var = 150 
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = img_blurred + gauss
    img_noisy = np.clip(noisy, 0, 255).astype(np.uint8)

    # 6. Simulasi Kompresi Stream JPEG ESP32 (Sangat Penting)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60] 
    result, encimg = cv2.imencode('.jpg', img_noisy, encode_param)
    img_final = cv2.imdecode(encimg, 1)

    # 7. Simpan gambar hasil augmentasi
    cv2.imwrite(output_path, img_final)

# ==========================================
# PENGATURAN FOLDER UTAMA
# ==========================================
folder_dataset_utama = 'dataset'
folder_output_utama = 'dataset_esp32'

# Daftar subfolder kategori yang ada di dalam dataset
kategori_folder = ['Animal','Branch', 'Car', 'Human', 'Motorcycle', 'Tree', 'Ocean']

print("Memulai proses augmentasi massal untuk simulasi ESP32...")

# Looping untuk masuk ke setiap subfolder kategori
for kategori in kategori_folder:
    path_input_kategori = os.path.join(folder_dataset_utama, kategori)
    path_output_kategori = os.path.join(folder_output_utama, kategori)
    
    # Buat folder output kategori jika belum ada (misal: dataset_esp32/Cars)
    if not os.path.exists(path_output_kategori):
        os.makedirs(path_output_kategori)
        
    # Kumpulkan semua file gambar dengan berbagai kemungkinan ekstensi
    list_gambar = []
    for ekstensi in ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG'):
        list_gambar.extend(glob.glob(os.path.join(path_input_kategori, ekstensi)))
        
    print(f"\nMemproses folder '{kategori}' - Ditemukan {len(list_gambar)} gambar.")
    
    # Looping untuk memproses dan menyimpan setiap gambar
    for path_gambar in list_gambar:
        nama_file = os.path.basename(path_gambar)
        path_simpan = os.path.join(path_output_kategori, "esp32_" + nama_file)
        
        proses_gambar_esp32(path_gambar, path_simpan)

print("\nProses augmentasi selesai! Dataset siap digunakan.")