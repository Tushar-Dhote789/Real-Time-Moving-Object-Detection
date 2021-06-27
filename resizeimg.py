import cv2
import imutils
img=cv2.imread("python.jpg")
resizeimg=imutils.resize(img,width=20)
cv2.imwrite("REsizedImg.jpg",resizeimg)
cv2.imshow("new image",resizeimg)
