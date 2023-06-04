import cv2
image=cv2.imread("earth.jpg",1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(400,400),(0,255,0),4)
cv2.circle(image,(200,200),100,(0,0,255),-1)
cv2.putText(image,"hello",(100,100),4,(10,56,167))
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


