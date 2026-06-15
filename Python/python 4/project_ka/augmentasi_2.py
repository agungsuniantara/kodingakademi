import cv2
import numpy as np
import os
import glob

def terapkan_efek_webcam(img):
    """
    Fungsi untuk memberikan efek webcam pada gambar array (bukan dari path).
    Asumsi gambar input sudah berukuran 640x480.
    """
    # 1. Efek Blur Sangat Ringan
    img_blurred = cv2.GaussianBlur(img, (3, 3), 0)

    # 2. Tambahkan Noise Sensor Ringan
    row, col, ch = img_blurred.shape
    mean = 0
    var = 20 
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = img_blurred + gauss
    img_noisy = np.clip(noisy, 0, 255).astype(np.uint8)

    # 3. Simulasi Kompresi Stream JPEG Webcam
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 85] 
    result, encimg = cv2.imencode('.jpg', img_noisy, encode_param)
    img_final = cv2.imdecode(encimg, 1)

    return img_final

# ==========================================
# PENGATURAN FOLDER UTAMA
# ==========================================
folder_gizi_baik = os.path.join('bayi', 'gizi baik')
folder_kurang_gizi = os.path.join('bayi', 'kurang gizi')
folder_output = 'bayi_gabungan_webcam'

# Buat folder output jika belum ada
if not os.path.exists(folder_output):
    os.makedirs(folder_output)

# Ambil semua path gambar dari kedua folder
# (Menggunakan sorted agar pasangannya berurutan dan konsisten)
list_gizi_baik = sorted(glob.glob(os.path.join(folder_gizi_baik, '*.[jp][pn]*[gG]')))
list_kurang_gizi = sorted(glob.glob(os.path.join(folder_kurang_gizi, '*.[jp][pn]*[gG]')))

print(f"Ditemukan {len(list_gizi_baik)} gambar gizi baik dan {len(list_kurang_gizi)} gambar kurang gizi.")
print("Memulai proses penggabungan dan augmentasi...")

# Gunakan zip untuk memasangkan gambar 1 per 1 dari kedua list
# Catatan: Jika jumlah gambar berbeda, zip akan berhenti di jumlah gambar yang paling sedikit
for i, (path_baik, path_kurang) in enumerate(zip(list_gizi_baik, list_kurang_gizi)):
    
    # 1. Baca kedua gambar
    img_baik = cv2.imread(path_baik)
    img_kurang = cv2.imread(path_kurang)
    
    if img_baik is None or img_kurang is None:
        print(f" -> Lewati pasangan {i+1} karena ada gambar yang gagal dibaca.")
        continue

    # 2. Resize masing-masing gambar menjadi setengah lebar resolusi VGA (320x480)
    img_baik_resized = cv2.resize(img_baik, (320, 480))
    img_kurang_resized = cv2.resize(img_kurang, (320, 480))

    # 3. Gabungkan gambar secara horizontal (kiri: gizi baik, kanan: kurang gizi)
    # Hasil akhir menjadi 640x480
    img_gabungan = np.hstack((img_baik_resized, img_kurang_resized))

    # 4. Terapkan efek webcam ke gambar gabungan
    img_hasil_akhir = terapkan_efek_webcam(img_gabungan)

    # 5. Simpan gambar
    nama_file_simpan = f"gabungan_webcam_{i+1}.jpg"
    path_simpan = os.path.join(folder_output, nama_file_simpan)
    cv2.imwrite(path_simpan, img_hasil_akhir)
    
    print(f"Tersimpan: {nama_file_simpan}")

print("\nProses selesai! Gambar gabungan siap digunakan.")