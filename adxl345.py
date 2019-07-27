'''
ADXL345 integration with motor
Author: Peter Chan
License: GNU General Public Domain
Jul 2019

CREDIT:

ADXL345 code
# Simple demo of of the ADXL345 accelerometer library.  Will print the X, Y, Z
# axis acceleration values every half second.
# Author: Tony DiCola
# License: Public Domain
'''

import RPi.GPIO as GPIO             # import GPIO module
import time
import Adafruit_ADXL345             # import the ADXL345 module
import motor as mv                  # import motor related modules


class ADXL345:

    def __init__(self):
        ### ADXL345 coding
        # Create an ADXL345 instance with I2C bus parameters
        self.accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=1)
        
    def roll_car(self,motor):
        m_status = motor.m_status
        rgb_status = motor.rgb_status
        roll = [0.0]*5
        for r in range(5):
            # Read the X, Y, Z axis acceleration values and print them.
            x, y, z = motor.adxl345.accel.read()
            roll[r] = x
            time.sleep(0.05)
        avRoll = int (sum(roll)/len(roll))
        if abs(avRoll) > 30.0:
            motor.rgb_bulb.led_RGB_setColor((255,69,0))         # dark orange
            motor.mt7219.led_matrix(chr(30))
            time.sleep(0.1)
            print ('Roll value > abs(30): ',avRoll)
        else:
            motor.rgb_bulb.led_RGB_setColor(rgb_status)         # restore original colour
            if m_status == 'Up/FF':                             # restore the LED Matrix
                motor.mt7219.led_matrix(chr(24))
            elif m_status == 'Down/BK':
                motor.mt7219.led_matrix(chr(25))
            elif m_status == 'Left/LF':
                motor.mt7219.led_matrix(chr(27))
            elif m_status == 'Right/RT':
                motor.mt7219.led_matrix(chr(26))
            elif m_status == 'Stop/SS':
                motor.mt7219.led_matrix(chr(120))
            elif m_status == 'Init/IN':
                motor.mt7219.led_matrix(chr(79))
        ### ADXL345 coding

def main():

    global robot
    robot = mv.Motor()
    time.sleep(3)
    # robot.motor_triage('Up/FF')
    while True:
        robot.adxl345.roll_car(robot)
   
    
if __name__ == '__main__':

        try:
            main()
        except KeyboardInterrupt:
            pass
        finally:
            robot.motor_close()
            GPIO.cleanup()

