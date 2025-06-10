import cv2 as cv
import numpy as np
from keras.models import load_model

#load the model (interference only)
model_path = "mask_detector.h5"
maskNet = load_model(model_path)

#process frame to match model input
def process_face(frame):
    face = cv.resize(frame, (224,224))
    face = face.astype("float32") / 255.0
    face = np.expand_dims(face, axis=0) # shape (1, 224, 224, 3)
    return face

# Get webcam footage
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    face_input = process_face(frame)
    prediction = maskNet(face_input)

    # interpret prediction: mask = 1, no mask = 0
    prob = float(prediction[0][0]) #adjust based on madel's shape
    label = "Mask" if prob > 0.5 else "No Mask"

    #draw label
    cv.putText(frame, f"{label} ({prob:.2f})", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if label == "Mask" else (0, 0, 255), 2)

    #display video
    cv.imshow("Face Mask Detection", frame)

    if cv.waitKey(1) == 27: #press 'ESC' to exit
        break

cap.release()
cv.destroyAllWindows()