import cv2
import time

# img = cv2.imread("resources/lena.png")
cap = cv2.VideoCapture("resources/lotus.mp4")
# cap = cv2.VideoCapture(0) #webcam read
# cap.set(3, 640) #width
# cap.set(4, 480) #height
# cap.set(10, 0) #brightness

while True:
    ok, img = cap.read()
    cv2.imshow("video (press q to close)", img)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    #make slow
    time.sleep(.09)

# cv2.imshow("output", img)
# cv2.waitKey(0)
