import cv2
import numpy as np

img = cv2.imread('book.jpg',cv2.IMREAD_COLOR)

retval, threshold = cv2.threshold(img,11,255,cv2.THRESH_BINARY)

cv2.imshow('org',img)
cv2.imshow('threshold',threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()