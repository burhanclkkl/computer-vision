import cv2
import numpy as np

img = cv2.imread("img.png")
img_grey = cv2.imread("img.png",0)

print("type:" + str(type(img)))
print(img)
print(img.size) #pixel (618*800*3 = 1483200)
print(img.dtype) # 0:black, 1:white
print(img.shape) #width, height, color channels

print(img_grey.shape) #width, height, color channels
print(img_grey)
