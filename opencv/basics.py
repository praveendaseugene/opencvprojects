import cv2
img=cv2.imread('earth.jpg',1)
cv2.imshow('earth',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
