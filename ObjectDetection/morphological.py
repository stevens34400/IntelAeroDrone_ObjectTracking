import cv2 as cv
import numpy as np
img = cv.imread('soccer.png',0)
kernel = np.ones((5,5),np.uint8)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

cv.imshow('image',gradient)
cv.waitKey(0)