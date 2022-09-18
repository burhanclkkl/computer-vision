import numpy as np
import cv2

img = cv2.imread('img.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = np.float32(grey)

corners = cv2.goodFeaturesToTrack(grey, 300, 0.01, 10)
corners = np.int0(corners)

number = 0
for i in corners:
    number = number + 1
    x,y = i.ravel()
    cv2.circle(img, (x,y), 1, (0,0,255), -1)
    cv2.putText(img, str(x) + ' '+ str(y),(x,y+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5,(0,0,255), 1)
    print(x,y)
    print(number)
cv2.imshow('corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()