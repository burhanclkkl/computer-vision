import cv2

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
save = cv2.VideoWriter('video_save.avi', fourcc, 60.0, (640,480))
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 0)
    
    if ret == True:
        save.write(frame)
        cv2.imshow("video capture", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()