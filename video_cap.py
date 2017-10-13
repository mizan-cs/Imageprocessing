import cv2

vdo = cv2.VideoCapture(0)
rec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',rec,20.0,(620,480))
while True:
    rt , frame = vdo.read()
    bw = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    cv2.imshow('Video',frame)
    cv2.imshow('BW',bw)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vdo.release()
out.release()
cv2.destroyAllWindows()