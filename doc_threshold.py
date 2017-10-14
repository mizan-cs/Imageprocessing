import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('th.PNG',cv2.IMREAD_COLOR)

ret, th1 = cv2.threshold(img,127,225)