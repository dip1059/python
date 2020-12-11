import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
cv2.circle(img,(265,265),10,(0,0,255),2)
cv2.ellipse(img, (328,265), (20,15), -50, 0, 360, (124,200,100), 2)

cv2.imshow("img", img)
cv2.waitKey(0)

