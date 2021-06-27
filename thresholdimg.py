import cv2
img=cv2.imread("python.jpg")
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshold=cv2.threshold(grayimg,150,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImg.jpg",threshold)
cv2.imshow("threshold image",threshold)
