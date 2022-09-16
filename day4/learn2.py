import cv2

img=cv2.imread('img.png')
cv2.imshow('img_orj', img)

cv2.rectangle(img,(150,200),(350,500),(250,0,0),10)
cv2.line(img,(200,200),(400,200),(0,0,250),5)
cv2.circle(img,(200,200),250,(0,250,250),8)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
