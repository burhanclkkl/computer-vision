import cv2
import numpy as np

def main():
    img=np.zeros((640,720,3),np.uint8)
    img.fill(1)
    
    fontscale = 0.7
    color=(255,0,255)
    
    cv2.putText(img, 'FONT_HERSHEY_COMPLEX', (20,50),cv2.FONT_HERSHEY_COMPLEX, fontscale, color)
    cv2.putText(img, 'FONT_HERSHEY_COMPLEX_SMALL', (20,90),cv2.FONT_HERSHEY_COMPLEX_SMALL, fontscale, color)
    cv2.putText(img, 'FONT_HERSHEY_DUPLEX', (20,130),cv2.FONT_HERSHEY_DUPLEX, fontscale, color)
    cv2.putText(img, 'FONT_HERSHEY_PLAIN', (20,170),cv2.FONT_HERSHEY_PLAIN, fontscale, color)
    cv2.putText(img, 'FONT_HERSHEY_SCRIPT_COMPLEX', (20,210),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, fontscale, color)
    cv2.putText(img, 'FONT_HERSHEY_SCRIPT_SIMPLEX', (20,250),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontscale, color)
    cv2.putText(img, 'FONT_HERSHEY_TRIPLEX', (20,290),cv2.FONT_HERSHEY_TRIPLEX, fontscale, color)
    cv2.putText(img, 'FONT_ITALIC', (20,330),cv2.FONT_ITALIC, fontscale, color)
        
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__ == '__main__':
    main()
