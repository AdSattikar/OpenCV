import cv2
import imutils
vc = cv2.VideoCapture(1)

while True:
    _,img = vc.read()
    img = imutils.resize(img, width=200)
    cv2.imshow("Video Stream", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("x"):
        break
vc.release()
cv2.destroyAllWindows()