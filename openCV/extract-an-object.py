import cv2
import numpy as np
import helpers

img = cv2.imread("resources/card.jpg")

width, height = 100,200
pts1 = np.float32([[336,62],[462,115],[384,313],[253,255]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

imgStack = helpers.stackImages(0.8, ([img],[imgOutput]))
cv2.imshow("extract.jpg", imgStack)
cv2.waitKey(0)

