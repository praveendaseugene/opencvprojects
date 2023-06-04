import cv2
image=cv2.imread("image1.jpg",20)
cv2.rectangle(image,(100,100),(500,500),(0,255,0),4)
font=cv2.FONT_HERSHEY_SIMPLEX
thikness=30
cv2.putText(image,"hello",(150,320),font,4,(10,56,167))
cv2.circle(image,(100,100),100,(255,255,255),1)
cv2.circle(image,(500,500),100,(255,255,255),1)
cv2.circle(image,(100,500),100,(255,255,255),1)
cv2.circle(image,(500,100),100,(255,255,255),1)
cv2.line(image,(0,0),(1000,1000),(255,0,0),5)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
