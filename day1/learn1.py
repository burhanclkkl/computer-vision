import cv2

img = cv2.imread('img.png', )
img_grey = cv2.imread('img.png', 0) # grey

cv2.imwrite('img_grey.png', img_grey)
cv2.imshow('Photo', img)
cv2.imshow('Photo Grey', img_grey)

cv2.waitKey(0)
cv2.destroyAllWindows()