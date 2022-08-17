import cv2
import imutils
import time

# cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# where img = image
#     x,y = start x start y 
#     x+w y+h end points
#     color, thickness

cam = cv2.VideoCapture(0)
time.sleep(1)
firstFrame = None
area = 1000

while True:
    _,img = cam.read() #read first frame from camera
    text = "Normal as first frame "
    img = imutils.resize(img, width=500) #resize
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # COLOR TO GRAYSCALE IMAGE
    gaussianImg = cv2.GaussianBlur(grayImg,(21,21),0) #Smoothen the image

    if firstFrame is None:
        firstFrame = gaussianImg
        continue
    imgDiff = cv2.absdiff(firstFrame, gaussianImg) #absolute difference between first and current frame
    threshImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1] #convert to binary as in 0 and 1 for black and white
    threshImg = cv2.dilate(threshImg, None ,iterations=2) # Fill up the remaining holes 
    cnts = cv2.findContours(threshImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #find nearby pixels to grab the nearby area of the moving image
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        print(text)
        if cv2.contourArea(c)< area:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text = "Moving Object Detected"
        print(text)
        cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("Camera Feed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("x"):
        break
cam.release()
cv2.destroyAllWindows()
