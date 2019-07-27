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
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
   ret,frame = cam.read()
   frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   cv2.imshow ('Original',frame)
   # Determine the lower boundary and upper boundary of HSV mask   
   l_h = cv2.getTrackbarPos("LH", "Tracking")
   l_s = cv2.getTrackbarPos("LS", "Tracking")
   l_v = cv2.getTrackbarPos("LV", "Tracking")
   u_h = cv2.getTrackbarPos("UH", "Tracking")
   u_s = cv2.getTrackbarPos("US", "Tracking")
   u_v = cv2.getTrackbarPos("UV", "Tracking")
   l_b = np.array([l_h, l_s, l_v])
   u_b = np.array([u_h, u_s, u_v])
   # Create image mask of the target image
   image_mask = cv2.inRange(frameHSV,l_b,u_b)
   cv2.imshow('image_mask',image_mask)
   if cv2.waitKey(1) == 27:
       break

cam.release()
cv2.destroyAllWindows()
