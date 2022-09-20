import cv2
from skimage import io

link = input('link: ')

img = io.imread(link)
cv2.imshow('img', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()
