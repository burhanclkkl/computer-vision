import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    area = frame[250:500,250:500]
        
        
    cv2.imshow('video', frame)
    cv2.imshow('video_area', area)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()
