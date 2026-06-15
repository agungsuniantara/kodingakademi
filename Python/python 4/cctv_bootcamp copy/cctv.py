import cv2
from ultralytics import YOLO

def main():
    model_path = 'models/best.pt'

    video_source = "rtsp://admin:Petro@2025@10.14.66.83:554/Streaming/Channels/102"

    conf_threshold = 0.25
    
    try:
        model = YOLO(model_path)
    except Exception as e:
        print(f"Error saat memuat model: {e}")
        return

    print(f"Mencoba membuka aliran video di: {video_source}")
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print(f"Error: Tidak dapat membuka sumber video di '{video_source}'")
        return

    print("Aliran video berhasil dibuka. Tekan 'q' pada jendela video untuk keluar.")

    while True:
        success, frame = cap.read()

        if not success:
            print("Aliran video berakhir atau terjadi error.")
            break
        else:
            frame = cv2.resize(frame, (640, 480)) 

        results = model(frame, conf=conf_threshold, verbose=False)

        annotated_frame = results[0].plot()

        cv2.imshow("Deteksi CCTV Real-time", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Program dihentikan.")

if __name__ == "__main__":
    main()