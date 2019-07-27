'''
Ultrasonic HC-SR04 measure distance
Author: Peter Chan
License: GNU General Public Domain
Jul 2019
'''

#Libraries
import RPi.GPIO as GPIO
import time
 

class Sonic:

    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)                      # GPIO Mode (BOARD / BCM)
        self.GPIO_TRIGGER = 20                      # set GPIO Pins
        self.GPIO_ECHO = 21                                      
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)     # set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
 
    def distance(self):
    
        GPIO.output(self.GPIO_TRIGGER, True)        # set Trigger to HIGH
        time.sleep(0.00001)                         # set Trigger after 0.01ms to LOW
        GPIO.output(self.GPIO_TRIGGER, False)
        startTime = time.time()
        stopTime = time.time()
        while GPIO.input(self.GPIO_ECHO) == 0:      # save start time
            startTime = time.time()
        while GPIO.input(self.GPIO_ECHO) == 1:      # save time of arrival
            stopTime = time.time()
        timeElapsed = stopTime - startTime          # time difference between start and arrival
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (timeElapsed * 34300) / 2

        return distance

def main():

    HC_SR04 = Sonic()
    while True:
        dist = HC_SR04.distance()
        print ("Measured Distance = %.1f cm" % dist)
        time.sleep(0.5)
      
if __name__ == '__main__':
    try:
        main()
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()



        
