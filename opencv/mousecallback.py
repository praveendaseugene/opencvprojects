import cv2

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x, y), 100, (255, 0, 0), -1)

image = cv2.imread("image1.jpg", 1)
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_circle)

while True:
    cv2.imshow('image', image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27: # Exit when "Esc" key is pressed
        break

cv2.destroyAllWindows()












