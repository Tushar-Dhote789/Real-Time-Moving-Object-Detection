import cv2
import time
cam=cv2.VideoCapture(0)
#cam=cv2.VideoCapture(0) for internal camera
#cam=cv2.VideoCapture(1) for external camera
time.sleep(1)

_,img=cam.read()
cv2.imwrite("cameraimg.jpg",img)
cam.release()

