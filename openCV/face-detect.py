import cv2

face_cascade = cv2.CascadeClassifier('venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
img = cv2.imread('resources/lena.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray,1.3,3)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 3)

cv2.imshow("out", img)
cv2.waitKey(0)
