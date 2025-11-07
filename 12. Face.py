import cv2
import dlib
import numpy as np
from PIL import Image

# Load face recognition models from dlib
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("F:\\OpenCV\\Dlib\\shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("F:\\OpenCV\\Dlib\\dlib_face_recognition_resnet_model_v1.dat")

# Load images and corresponding names
image_paths = [
    "F://OpenCV//Images//m1.jpg",
    "F://OpenCV//Images//m2.jpg",
    "F://OpenCV//Images//m3.jpg"
]
known_face_names = ["ELON", "BILL", "MARK"]

known_face_encodings = []

for image_path in image_paths:
    # Load image using Pillow
    image = Image.open(image_path)
    
    # Convert image to RGB and ensure it's in 8-bit format
    image_rgb = image.convert('BGR')
    image_rgb = np.array(image_rgb)
    

    
    # Detect faces in the image
    image_rgb = np.array(image_rgb).astype(np.uint8)
    faces = detector(image_rgb)
    
    if len(faces) == 0:
        print(f"No face found in the image {image_path}")
        continue
    
    # Get the landmarks/parts for the face
    shape = shape_predictor(image_rgb, faces[0])
    
    # Get the face encoding
    face_encoding = face_recognizer.compute_face_descriptor(image_rgb, shape)
    
    # Append encoding to known face encodings list
    known_face_encodings.append(np.array(face_encoding))

# Open video capture
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Unable to read frame from the camera.")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = detector(frame_rgb)

    for face in faces:
        shape = shape_predictor(frame_rgb, face)
        face_encoding = face_recognizer.compute_face_descriptor(frame_rgb, shape)

        matches = np.linalg.norm(known_face_encodings - np.array(face_encoding), axis=1) < 0.6
        name = "Unknown"
        if np.any(matches):
            name = known_face_names[np.argmax(matches)]

        top, right, bottom, left = face.top(), face.right(), face.bottom(), face.left()
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(30) == 27:  # Exit the loop when 'ESC' key is pressed
        break

video_capture.release()
cv2.destroyAllWindows()
