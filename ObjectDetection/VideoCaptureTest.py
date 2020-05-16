import cv2
import numpy as np

im = cv2.VideoCapture(0)

while(True):
    #Capture fram-by-frame
    ret, frame = im.read()

    #Our operations on the frame come here
    #gray=cv2.cvtColor(frame, convertBGR2GRAY)

    #Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture
im.release()
cv2.destroyAllWindows()