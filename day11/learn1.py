import cv2, numpy as np

face_cascade = cv2.CascadeClassifier('face.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 1)
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eye = eye_cascade.detectMultiScale(roi_grey,1.3,1)
        for (ex, ey, ew, eh) in eye:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 1)
            eye_ = roi_color[ey:ey+eh, ex:ex+ew]
            cv2.imshow('roi_color', eye_)
            
            
            
    cv2.flip(frame, 1)
    cv2.imshow('camera', frame)
       
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()