import cv2
img=cv2.imread("python.jpg")
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("graypython.jpg",grayimg)
cv2.imshow("Original image",img)
cv2.imshow(" converted image",grayimg)
cv2.waitKey(0)
cv2.destroyAllWindow()
           
