import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('E:\im.PNG',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(97,97),(78,65,97),10)
cv2.rectangle(img,(100,100),(300,300),(0,225,0),5)
cv2.circle(img,(200,200),100,(0,0,255),3)

shape = np.array([[56,13],[34,62],[12,45],[17,77]],np.int32)
cv2.polylines(img,[shape],True,(0,255,0),3)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'Mizan',(300,300),font,1,(0,0,255),1)

plt.imshow(img)
plt.show()

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()