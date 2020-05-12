import cv2
import numpy as np

im = cv2.VideoCapture(0)

while(True):
    #Capture frame-by-frame
    ret, frame = im.read()

    #median blur
    frame = cv2.medianBlur(frame, 5)

    if not ret:
        break

    #Convert BGR to HSV
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Define range of red
    lower_red = np.array([140, 70, 70])
    upper_red = np.array([180, 255, 255])
    mask = cv2.inRange(img_hsv, lower_red, upper_red)

    output_img = frame.copy()
    output_img[np.where(mask == 0)] = 0

    output_hsv = frame.copy()
    output_hsv[np.where(mask == 0)] = 0
    canvas = frame.copy()

    #Erosion then dillation
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


    #Define Contour
    try:
        _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        #Find Centroid of moving object
        blob = max(contours, key=lambda el: cv2.contourArea(el))
        M =cv2.moments(blob)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        cv2.circle(canvas, center, 7, (255, 0, 0), -1)

        #Draw contour around red object
        cv2.drawContours(canvas, contours, -1, (255,255,0),3)

    except(ValueError, ZeroDivisionError):
        pass

    #Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow("canvas", canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture
im.release()
cv2.destroyAllWindows()