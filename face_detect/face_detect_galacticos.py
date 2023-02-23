import cv2

# 모델 객체 생성
path = "haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(path)

# image load
image_path = "galacticos.jpg"
image = cv2.imread(image_path)

# 모델이 얼굴 좌표와 너비 높이를 탐지함
# faces에 탐지된 정보(x, y, w, h)들이 들어감
faces = face_detector.detectMultiScale(image)


# 박스 그려주기
for face in faces:
    (x, y, w, h) = face
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 3)

# 얼굴에 점 찍힌 이미지 띄우기
cv2.imshow('face detection, box!', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
