import numpy as np
import cv2 as cv

green = np.uint8([[[230,50,0]]])
hsv_green=cv.cvtColor(green,cv.COLOR_BGR2HSV)
print(hsv_green)
