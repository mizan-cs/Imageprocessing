import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_red = np.array([110,50,50])
    h_red = np.array([130,255,255])

    mask = cv2.inRange(hsv,l_red,h_red)
    res = cv2.bitwise_and(frame,hsv,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('hsv',hsv)

    if cv2.waitKey(3) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()