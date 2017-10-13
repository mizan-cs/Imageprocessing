import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('E:\im.PNG',cv2.IMREAD_COLOR)

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()