import cv2, numpy as np

cam = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('face.xml')

while(1):
    ret, frame = cam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255), 1)
        roi = frame[y:y+h, x:x+w]

    cv2.imshow('roi', roi)
    cv2.imshow('cam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()
