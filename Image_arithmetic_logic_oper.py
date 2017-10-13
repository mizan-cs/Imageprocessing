import cv2

img1 = cv2.imread('img1.PNG',cv2.IMREAD_COLOR)
img2 = cv2.imread('python.PNG',cv2.IMREAD_COLOR)

row, col, channels = img2.shape
roi = img1[0:row, 0:col]

im2gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)

ret, mask = cv2.threshold(im2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img2_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img2_bg,img2_fg)
img1[0:row, 0:col] = dst

cv2.imshow('res',img1)




cv2.waitKey(0)
cv2.destroyAllWindows()