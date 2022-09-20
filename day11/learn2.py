from lib2to3.pgen2 import grammar
import cv2, numpy as np

cam = cv2.VideoCapture('video.mp4')
fullbody = cv2.CascadeClassifier('fullBody.xml')
while True:
    ret, frame = cam.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    full_body = fullbody.detectMultiScale(grey,1.9,1)
    
    for x,y,w,h in full_body:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 1)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()