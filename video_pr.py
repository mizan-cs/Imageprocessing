import cv2

vdo = cv2.VideoCapture(0)

while True:
    res, frame = vdo.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    gaus = cv2.adaptiveThreshold(gray, 150, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 125, 3)

    cv2.imshow('video',frame)
    cv2.imshow('gray', gray)
    cv2.imshow('threshold', gaus)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vdo.release()
cv2.destroyAllWindows()
