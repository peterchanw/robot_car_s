import numpy as np                  # import Numpy
import cv2                          # import OpenCV
import matplotlib.pyplot as plt     # import matplotlib for plotting
import time
import RPi.GPIO as GPIO

def opcv_init():
    cam = cv2.VideoCapture(0)   # create camera object
    w=640
    h=480
    cam.set(3,w)                # set cam to (640x480) resolution
    cam.set(4,h)
    return cam

def opcv_main():
    cam = opcv_init()
    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imshow('Original',frame)
            image = frame.copy()
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray,(5,5),0)
            ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
            kernal = np.ones((3,3), np.uint8)
            thresh = cv2.erode(thresh,kernal,iterations=3)
            thresh = cv2.dilate(thresh,kernal,iterations=3)
            mask = np.zeros_like(thresh)
            mask[200:480,0:639] = 1
            output = cv2.bitwise_and(thresh,thresh, mask=mask)
            img,contours,hierarchy = cv2.findContours(output,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                c = max(contours, key=cv2.contourArea)
                M = cv2.moments(c)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(image,(cx,cy),7,(255,0,0),-1)
                cv2.drawContours(image,contours,-1,(0,255,0),3)
                setPoint = 320
                error = cx - setPoint
                cv2.putText(image,str(error),(10,280),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)  
                l_box = cv2.minAreaRect(c)
                (x2,y2),(w2,h2),ang = l_box
                ang = int(ang)
                box = cv2.boxPoints(l_box)
                box = np.int0(box)
                cv2.drawContours(image,[box],0,(0,0,255),3)
                cv2.putText(image,str(ang),(10, 200), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            cv2.imshow('Process',image)
            key = cv2.waitKey(1)
            if key == 27:
                cam.release()
                break
          
    
if __name__ == '__main__':
    try:
        opcv_main()
        
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
