from keras.models import load_model
import cv2
import numpy as np
import h5py

np.set_printoptions(suppress=True)

f = h5py.File("/Applications/MAMP/htdocs/local/kodingakademi/Python/taman rama/converted_keras/keras_model.h5", mode="r+")
model_config_string = f.attrs.get("model_config")

if model_config_string.find('"groups": 1,') != -1:
    model_config_string = model_config_string.replace('"groups": 1,', '')
f.attrs.modify('model_config', model_config_string)
f.flush()
model_config_string = f.attrs.get("model_config")
assert model_config_string.find('"groups": 1,') == -1

model = load_model("/Applications/MAMP/htdocs/local/kodingakademi/Python/taman rama/converted_keras/keras_model.h5", compile=False)
class_names = open("/Applications/MAMP/htdocs/local/kodingakademi/Python/taman rama/converted_keras/labels.txt", "r").readlines()

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Gagal membuka kamera. Coba cek koneksi kamera.")
        break

    frame_display = cv2.resize(frame, (480, 480), interpolation=cv2.INTER_AREA)

    image = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    img_predict = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    img_predict = (img_predict / 127.5) - 1

    prediction = model.predict(img_predict)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    label = f"{class_name.strip()}: {confidence_score*100:.1f}%"
    cv2.putText(
        frame_display, label, (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2
    )

    cv2.imshow("Webcam Image", frame_display)

    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
