import cv2
import os

# Path to the video file
video_path = 'video/vidio.mp4'

# Directory to save the frames
output_folder = 'frames'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read until the video is completed
frame_count = 0
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        frame_name = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_name, frame)
        frame_count += 1
    else:
        break

# When everything done, release the video capture object
cap.release()

print(f"Successfully extracted {frame_count} frames to '{output_folder}' folder.")
