import cv2
import numpy as np

cam = cv2.VideoCapture(0)

low = np.array([90, 50, 50])
high = np.array([255, 130, 255])

while (1):
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    hsv = cv2.flip(hsv, 1)
    mask = cv2.inRange(hsv, low, high) 
    
    mask = cv2.flip(mask, 1)
    cv2.imshow('video', frame)
    
    bitwise_and = cv2.bitwise_and(frame, frame, mask=mask)
    bitwise_and = cv2.flip(bitwise_and,1)
    
    cv2.imshow('bitwise_and',bitwise_and)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
