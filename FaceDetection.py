import cv2

alg = "haarcascade_frontalface_default.xml"
haar_casacde = cv2.CascadeClassifier(alg)

vc = cv2.VideoCapture(0)

while True:
    _,img = vc.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_casacde.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face Detection",img)
    key = cv2.waitKey(2) & 0xFF
    if key == ord("x"):
        break
vc.release()
cv2.destroyAllWindows()