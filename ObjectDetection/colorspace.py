import cv2 as cv
import numpy as np

img = cv.imread("red1.png")
img_hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)

#lower mask(0-10)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv.inRange(img_hsv, lower_red, upper_red)

# Upper
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv.inRange(img_hsv,lower_red,upper_red)

mask = mask0+mask1

output_img = img.copy()
output_img[np.where(mask==0)] = 0

output_hsv = img.copy()
output_hsv[np.where(mask==0)] = 0

cv.imshow('img',img)
cv.imshow('mask', mask1)
cv.waitKey(0)