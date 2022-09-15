import cv2
import numpy as np

img=cv2.imread('img.png')

img1= cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REPLICATE)
img2= cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REFLECT_101)
img3= cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REFLECT)
img4= cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_WRAP)
img5= cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_CONSTANT)

cv2.imshow('img', img)
cv2.imshow('BORDER_REPLICATE', img1)
cv2.imshow('BORDER_REFLECT_101', img2)
cv2.imshow('BORDER_REFLECT', img3)
cv2.imshow('BORDER_WRAP', img4)
cv2.imshow('BORDER_CONSTANT', img5)

cv2.waitKey(0)
cv2.destroyAllWindows()