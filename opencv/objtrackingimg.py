import cv2
import numpy as np

image=cv2.imread('img.jpg',1)
new_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",new_image)
lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])
mask=cv2.inRange(new_image,lower_blue,upper_blue)
cv2.imshow("mask",mask)
result=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('res',result)

cv2.waitKey(0)
cv2.destroyAllWindows()



















