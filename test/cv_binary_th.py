import numpy as np
import cv2

def nothing(x):
    pass

# Read the target with the resolution (320 x 240)
cam = cv2.VideoCapture(0)   # create camera object
w=640
h=480
cam.set(3,w)                # set cam to (640x480) resolution
cam.set(4,h)

# Define the HSV setting control window
cv2.namedWindow("Tracking")
cv2.createTrackbar("LB", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UB", "Tracking", 255, 255, nothing)

while True:
   ret,frame = cam.read()
   frameGRAY = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   cv2.imshow ('Original',frame)
   # Determine the lower boundary and upper boundary of HSV mask   
   l_b = cv2.getTrackbarPos("LB", "Tracking")
   u_b = cv2.getTrackbarPos("UB", "Tracking")
   # Create image mask of the target image
   ret, image_mask = cv2.threshold(frameGRAY,l_b,u_b,cv2.THRESH_BINARY)
   # Automatic adjustments to get the optimum threshold of B&W image due to changing light conditions
#   ret, image_mask = cv2.threshold(frameGRAY,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
   cv2.imshow('image_mask',image_mask)
   if cv2.waitKey(1) == 27:
       break

cam.release()
cv2.destroyAllWindows()
