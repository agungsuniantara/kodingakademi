import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import numpy as np
import time
from PIL import Image

st.title("Real-time APD Detection")
st.write("Aplikasi deteksi APD menggunakan YOLOv8")

# Sidebar controls
with st.sidebar:
    st.header("Settings")
    model_path = st.selectbox(
        "Model Path",
        ['models/best.pt', 'runs/detect/train4/weights/best.pt'],
        index=1
    )
    conf_threshold = st.slider("Confidence Threshold", 0.1, 1.0, 0.25)
    run_detection = st.button("Start Detection")

# Placeholder for video feed
placeholder = st.empty()

if run_detection:
    try:
        # Load model
        with st.spinner("Loading model..."):
            model = YOLO(model_path)

        st.success("Model loaded successfully!")

        # Initialize webcam
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("Cannot access webcam. Please check if webcam is available.")
        else:
            st.info("Starting detection... Press 'Stop Detection' to quit.")

            stop_button = st.button("Stop Detection")

            while not stop_button:
                ret, frame = cap.read()
                if not ret:
                    st.error("Failed to read frame from webcam.")
                    break

                # Perform detection
                results = model(frame, conf=conf_threshold, verbose=False)

                # Get annotated frame
                annotated_frame = results[0].plot()

                # Convert BGR to RGB for Streamlit
                rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

                # Display frame
                placeholder.image(rgb_frame, channels="RGB", use_container_width=True)

                # Small delay to prevent overwhelming the interface
                time.sleep(0.1)

            cap.release()
            st.info("Detection stopped.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Click 'Start Detection' in the sidebar to begin real-time APD detection.")

# Footer
st.markdown("---")
st.markdown("**APD Detection App** - Powered by YOLOv8 and Streamlit")
