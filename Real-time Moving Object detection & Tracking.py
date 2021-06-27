import imutils
import cv2
import time

cam=cv2.VideoCapture(0)
time.sleep(1)

firstFrame=None
area=500

while True:
    _,img=cam.read()
    #_,img : return two values in which first is not useful for use
    # thats why we skip first value and store second value in img variable

    # img= cam.read() [1] (we can write it too)
    
    text="Normal"
    img=imutils.resize(img,width=500)
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussianImg=cv2.GaussianBlur(grayImg,(1,1),0)
    if firstFrame is None:
        firstFrame=grayImg
        continue
    imgDiff=cv2.absdiff(firstFrame,grayImg)

    threshImg=cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]
    threshImg=cv2.dilate(threshImg,None,iterations=2)
     #dilute: to dilute pixels, fill white dots in threshold images

    cnts=cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
      #Counters: it is used to connect, disconnected threshold image  
    cnts=imutils.grab_contours(cnts)
     #cnts: it will give grab that area;
     #how much area in cnts?  is it skipable or shall I fill that area

    for c in cnts:
         if cv2.contourArea(c) < area:
             continue
         (x,y,w,h)= cv2.boundingRect(c)
         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
         text = "Moving Object Detected"
    print(text)
    cv2.putText(img,text, (10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    cv2.imshow("cameraFeed",img)
   
    Key=cv2.waitKey(1)&0xFF
      
    if Key== ord("q"):
        break
      
cam.release()
cv2.destroyAllWindows()
 















                           
