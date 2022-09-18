import cv2
import numpy as np
from matplotlib import pyplot as plt

cam = cv2.VideoCapture(0)

while (1):
    ret, frame = cam.read()
    border = cv2.Canny(frame, 100,80)
    
    cv2.imshow('Capture', border)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()
    