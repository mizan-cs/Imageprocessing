import cv2
import numpy as np
import matplotlib.pyplot as plt

group_img = cv2.imread('group.jpg')
gray = cv2.cvtColor(group_img,cv2.COLOR_RGB2GRAY)

mizan_img = cv2.imread('mizan.jpg',0)

w, h = mizan_img.shape[::-1]

res = cv2.matchTemplate(gray,mizan_img,cv2.TM_CCOEFF_NORMED)
th = 0.7

loc = np.where(res >= th)

for pt in zip(*loc[::-1]):
    cv2.rectangle(group_img,pt,(pt[0]+w, pt[1]+h),(0,255,255),2)
#cv2.imshow('result',group_img)
plt.imshow(group_img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()