import cv2
from ultralytics import YOLO

def main():
    # --- PENGATURAN ---
    # Path ke model YOLOv8 Anda.
    # Pastikan path ini benar.
    model_path = 'runs/detect/train/weights/best.pt'
    # model_path = 'model_jadi/best.pt' # model tidak manual

    # Sumber video: 0 untuk webcam utama.
    video_source = 0

    # Ambang batas kepercayaan (turunkan untuk melihat lebih banyak deteksi).
    conf_threshold = 0.1
    # --- SELESAI PENGATURAN ---

    # Muat model
    try:
        model = YOLO(model_path)
    except Exception as e:
        print(f"Error saat memuat model: {e}")
        return

    # Buka koneksi ke webcam
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print(f"Error: Tidak dapat membuka kamera (sumber: {video_source})")
        return

    print("Kamera berhasil dibuka. Tekan 'q' pada jendela video untuk keluar.")

    # Loop untuk membaca frame dari kamera
    while True:
        success, frame = cap.read()
        if not success:
            print("Gagal membaca frame dari kamera.")
            break

        # Lakukan prediksi dengan confidence threshold yang sudah diatur
        # verbose=False untuk menyembunyikan log dari console
        results = model(frame, conf=conf_threshold, verbose=False)

        # Gambar hasil deteksi pada frame
        annotated_frame = results[0].plot()

        # Tampilkan frame
        cv2.imshow("Deteksi APD Real-time", annotated_frame)

        # Hentikan loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Lepaskan sumber daya
    cap.release()
    cv2.destroyAllWindows()
    print("Program dihentikan.")

if __name__ == "__main__":
    main()
