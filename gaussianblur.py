import cv2
img=cv2.imread("python.jpg")
gaussianimg=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussianimg.jpg",gaussianimg)
