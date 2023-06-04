import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while(1):
    _,frame=cap.read()

    new_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv",new_image)

    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    mask=cv2.inRange(new_image,lower_blue,upper_blue)
    # cv2.imshow("mask",mask)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('res',result)

    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
























