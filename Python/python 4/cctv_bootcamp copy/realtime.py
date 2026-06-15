import cv2
from ultralytics import YOLO

def main():
    model_path = 'models/best.pt'
    # model_path = 'runs/detect/train5/weights/best.pt'

    video_source = 0

    conf_threshold = 0.25
    
    model = YOLO(model_path)

    # Buka koneksi ke webcam
    cap = cv2.VideoCapture(video_source)

    while True:
        success, frame = cap.read()
        if not success:
            print("Gagal membaca frame dari kamera.")
            break

        results = model(frame, conf=conf_threshold, verbose=False)

        # Gambar hasil deteksi pada frame
        annotated_frame = results[0].plot()

        # Tampilkan frame
        cv2.imshow("Deteksi APD Real-time", annotated_frame)

        # Hentikan loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Program dihentikan.")

if __name__ == "__main__":
    main()
