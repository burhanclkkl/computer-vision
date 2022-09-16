import cv2
import numpy as np

cam = cv2.VideoCapture(0)

'''
def cam_setting():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
'''

def cam_setting(x, y = 50):
    width = int(x.shape[1] * y/100)
    height = int(x.shape[0] * y/100)
    size = (width, height)
    return cv2.resize(x,size,interpolation=cv2.INTER_AREA)

def main():
    while True:
        ret, frame = cam.read()
        frame2 = cam_setting(frame)
        grey = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        color1 = cv2.cvtColor(frame2, cv2.COLOR_BGR2YUV_IYUV)
        color2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2Lab)
        color3 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HLS_FULL)
        color4 = cv2.cvtColor(frame2, cv2.COLOR_BGR2YCrCb)
        color5 = cv2.cvtColor(frame2, cv2.COLOR_BGR2BGRA)
        
        cv2.imshow('frame', frame)
        cv2.imshow('frame2', frame2)
        cv2.imshow('grey', grey)
        cv2.imshow('color1', color1)
        cv2.imshow('color2', color2)
        cv2.imshow('color3', color3)
        cv2.imshow('color4', color4)
        cv2.imshow('color5', color5)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()