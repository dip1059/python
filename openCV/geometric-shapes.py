import cv2
import numpy as np
import helpers

img = cv2.imread("resources/shapes.jpg")
img_cont = img.copy()
img_canny = cv2.Canny(img, 50, 50)
conts, hacrh = cv2.findContours(img_canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for cont in conts:
    area = cv2.contourArea(cont)
    if area > 500 :
        # cv2.drawContours(img_cont,cont,-1,(0,0,0),3)
        perimeter = cv2.arcLength(cont, True)
        corners = cv2.approxPolyDP(cont,0.02*perimeter,True)
        # print(len(corners))
        corner_length = len(corners)
        x,y,w,h = cv2.boundingRect(corners)
        # cv2.rectangle(img_cont,(x,y),(x+w,y+h),(255,255,0),5)
        if corner_length == 3 : obj_type = "tri"
        elif corner_length == 4:
            aspect_ratio = w/float(h)
            if aspect_ratio > 0.95 and aspect_ratio < 1.05: obj_type = "square"
            else: obj_type = "rect"
        elif corner_length == 5: obj_type = "pentagon"
        elif corner_length == 6: obj_type = "hexagon"
        elif corner_length == 7: obj_type = "heptagon"
        elif corner_length == 8: obj_type = "circle"
        else: obj_type = "polygon"

        cv2.putText(img_cont, obj_type, (x+w//2,y+h//2), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0), 2)

all_img = helpers.stackImages(0.4, [img, img_cont])
cv2.imshow("out", all_img)
cv2.waitKey(0)
