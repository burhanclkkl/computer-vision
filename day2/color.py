import cv2
import numpy as np

img=cv2.imread("img.png")
x =0
for i in range(220):
    x = x+1
    img[60:80,i] = [255,255,x]
x =0
for i in range(220):
    x = x+1
    img[250:500,i] = [x,255,255]

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


