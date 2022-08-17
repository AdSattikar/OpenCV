import cv2 as cv
img = cv.imread('D:\OpenCV\IMG_20160507_212429_1462680462284.jpg')

cv.imshow('Adnan',img)
gaussianBlurImg = cv.GaussianBlur(img,(5,5),0)
cv.imwrite("Gaussianblur.jpg",gaussianBlurImg)
cv.waitKey(0)


