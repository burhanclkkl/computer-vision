import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low = np.array([100, 60, 60])
    high = np.array([140, 255, 255])
    
    mask = cv2.inRange(hsv, low, high)
    last_image = cv2.bitwise_and(hsv,hsv,mask = mask)
    
    kernel = np.ones((15,15), np.float32) / 255
    smoothed = cv2.filter2D(last_image, -1,kernel)
    
    blur = cv2.GaussianBlur(smoothed,(15,15),0)
    
    
    last_image = cv2.flip(last_image, 1)
    cv2.imshow("Video Camera", last_image)
    
    blur = cv2.flip(blur, 1)
    cv2.imshow("smoothed", blur)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()