import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

path = "haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(path)

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
write_path = "me_webcam"

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
size = (width, height)

fourcc = cv2.VideoWriter_fourcc('M','P','4','V')
out = cv2.VideoWriter(write_path, fourcc, fps, size)

font = cv2.FONT_HERSHEY_COMPLEX

while cap.isOpened():
    ret, frame = cap.read()
    faces = face_detector.detectMultiScale(frame)
    
    if ret:
        for face in faces:
            (x, y, w, h) = face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (155, 100, 0), 3)
        cv2.imshow('face detect', frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
            
cap.release()
out.release()
cv2.destroyAllWindows()
