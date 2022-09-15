import cv2
import numpy as np

img= cv2.imread('1.jpg')
img1= cv2.imread('2.jpg')

img_img1 = cv2.addWeighted(img, 0.7, img1, 0.1, 2)

cv2.imshow('img',img)
cv2.imshow('img1', img1)
cv2.imshow('img_img1', img_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()