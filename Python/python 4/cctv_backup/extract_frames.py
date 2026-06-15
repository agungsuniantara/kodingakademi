import cv2
import os

video_path = 'video/video2.mp4'

output_folder = 'datasets_video/train/images'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame_name = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_name, frame)
        frame_count += 1
    else:
        break

cap.release()

print(f"Successfully extracted {frame_count} frames to '{output_folder}' folder.")
