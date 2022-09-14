import cv2
import numpy as np

img = cv2.imread("img.png")
print(img.item(100,250,1)) #100,250,0 -- 0:blue 1:green 2:red

#roi
roi = img[65:250, 600:700] #[y1:y2, x1:x2]
cv2.imshow("roi", roi)

'''
img[65:250, 300:400] = roi

img[:,:,0] = 255
img[:,:,1] = 255
'''

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()