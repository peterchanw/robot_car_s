'''
Motor movement
Author: Peter Chan
License: GNU General Public Domain
Jul 2019

CREDITS:

MAX 7219 code
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# https://max7219.readthedocs.io/en/0.2.3/

LCD 1602 original code found at:
# https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
# Compiled, mashed and generally mutilated 2014-2015 by Denis Pleic
# Made available under GNU GENERAL PUBLIC LICENSE
#

ADXL345 code
# Simple demo of of the ADXL345 accelerometer library.  Will print the X, Y, Z
# axis acceleration values every half second.
# Author: Tony DiCola
# License: Public Domain
'''

import time
import RPi.GPIO as GPIO
import maxled as mLED                       # import MAX7219 related modules
import i2c_lcd_driver as lcd1602            # import LCD1602 related modules
import rgb                                  # import RGB led related modules
import ultrasonic as sc                     # import HC-SR04 related modules
import servo_motor as sv                    # import servo related modules
import adxl345 as adxl                      # import the ADXL345 module

class Motor:

    def __init__(self):                     # initiaize the Motor object
            
        ### left motor's pins
        self.in1 = 18  # lf_pin1
        self.in2 = 23  # lf_pin2
        # enA = x (left motor 'PWM' for speed - not used)
        ### right motor's pins
        self.in3 = 24  # rt_pin1
        self.in4 = 25  # rt_pin2
        # enB = y (right motor 'PWM' for speed - not used)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        self.lf_pin1 = 0
        self.lf_pin2 = 0
        self.rt_pin1 = 0
        self.rt_pin2 = 0
        GPIO.output(self.in1, self.lf_pin1)
        GPIO.output(self.in2, self.lf_pin2)
        GPIO.output(self.in3, self.rt_pin1)
        GPIO.output(self.in4, self.rt_pin2)
        self.p_status = 'Init/IN'                   # previous motor status
        self.p_rgb = (255,255,0)                    # previous rgb status - yellow
        self.m_status = 'Init/IN'                   # current motor status
        self.rgb_status = (255,255,0)               # current rgb status - yellow
        self.mt7219 = mLED.LED_mat()                # create max7219 object
        self.mt7219.led_matrix(chr(79))             # 'o' sign for readiness
        self.lcd = lcd1602.lcd()                    # create lcd1602 object
        self.lcd.backlight(1)                       # turn on the lcd1602 backlight 
        self.lcd.lcd_clear()                        # clear the display
        self.line = 'Robot Car      '               # display 'Robot Car' in LCD
        self.lcd.lcd_display_string(self.line,1)
        self.rgb_bulb = rgb.RGB_led()               # create RGB object
        self.rgb_bulb.led_RGB_setColor((255,255,0)) # yellow colour
        time.sleep(0.1)
        self.sonic = sc.Sonic_dev()                 # create the ultrasionic object
        self.servo = sv.Servo()                     # create the servo object
        self.adxl345 = adxl.ADXL345()               # create the ADXL345 object           
        print(self.m_status)

    def motor_ff(self):                             # motor moving forward

        self.lf_pin1 = 1
        self.lf_pin2 = 0
        self.rt_pin1 = 1
        self.rt_pin2 = 0
        GPIO.output(self.in1, self.lf_pin1)
        GPIO.output(self.in2, self.lf_pin2)
        GPIO.output(self.in3, self.rt_pin1)
        GPIO.output(self.in4, self.rt_pin2)
        self.m_status = 'Up/FF'                     # current motor status
        self.rgb_status = (0,255,0)                 # current rgb status - green
        self.mt7219.led_matrix(chr(24))             # Up arrow sign
        self.line = 'Forward/FF      '
        self.lcd.lcd_display_string(self.line,1)    # display 'Forward/FF' in LCD
        self.rgb_bulb.led_RGB_setColor((0,255,0))   # green colour
        time.sleep(0.1)
        print(self.m_status)

    def motor_bk(self):                             # motor moving backward

        self.lf_pin1 = 0
        self.lf_pin2 = 1
        self.rt_pin1 = 0
        self.rt_pin2 = 1
        GPIO.output(self.in1, self.lf_pin1)
        GPIO.output(self.in2, self.lf_pin2)
        GPIO.output(self.in3, self.rt_pin1)
        GPIO.output(self.in4, self.rt_pin2)
        self.m_status = 'Down/BK'                   # current motor status
        self.rgb_status = (255,0,0)                 # current rgb status - red
        self.mt7219.led_matrix(chr(25))             # Down arrow sign
        self.line = 'Backward/BK     '
        self.lcd.lcd_display_string(self.line,1)    # display 'Backward/BK' in LCD
        self.rgb_bulb.led_RGB_setColor((255,0,0))   # red colour
        time.sleep(0.1)
        print(self.m_status)

    def motor_lf(self):                             # motor turning left

        self.lf_pin1 = 1
        self.lf_pin2 = 0
        self.rt_pin1 = 0
        self.rt_pin2 = 1
        GPIO.output(self.in1, self.lf_pin1)
        GPIO.output(self.in2, self.lf_pin2)
        GPIO.output(self.in3, self.rt_pin1)
        GPIO.output(self.in4, self.rt_pin2)
        self.m_status = 'Left/LF'                   # current motor status
        self.rgb_status = (0,255,255)               # current rgb status - cyan
        self.mt7219.led_matrix(chr(27))             # Left arrow sign
        self.line = 'Left/LF         '
        self.lcd.lcd_display_string(self.line,1)    # display 'Left/LF' in LCD
        self.rgb_bulb.led_RGB_setColor((0,255,255)) # cyan colour
        time.sleep(0.1)
        print(self.m_status)

    def motor_rt(self):                             # motor turning right

        self.lf_pin1 = 0
        self.lf_pin2 = 1
        self.rt_pin1 = 1
        self.rt_pin2 = 0
        GPIO.output(self.in1, self.lf_pin1)
        GPIO.output(self.in2, self.lf_pin2)
        GPIO.output(self.in3, self.rt_pin1)
        GPIO.output(self.in4, self.rt_pin2)
        self.m_status = 'Right/RT'                  # current motor status
        self.rgb_status = (255,0,255)               # current rgb status - magenta
        self.mt7219.led_matrix(chr(26))             # right arrow sign
        self.line = 'Right/RT        '
        self.lcd.lcd_display_string(self.line,1)    # display 'Right/RT' in LCD
        self.rgb_bulb.led_RGB_setColor((255,0,255)) # magenta colour
        time.sleep(0.1)
        print(self.m_status)

    def motor_ss(self):

        self.lf_pin1 = 0
        self.lf_pin2 = 0
        self.rt_pin1 = 0
        self.rt_pin2 = 0
        GPIO.output(self.in1, self.lf_pin1)
        GPIO.output(self.in2, self.lf_pin2)
        GPIO.output(self.in3, self.rt_pin1)
        GPIO.output(self.in4, self.rt_pin2)
        self.m_status = 'Stop/SS'                   # current motor status
        self.rgb_status = (255,255,255)             # current rgb status - white
        self.mt7219.led_matrix(chr(120))            # cross sign
        self.line = 'Stop/SS         '
        self.lcd.lcd_display_string(self.line,1)    # display 'Stop/SS' in LCD
        self.rgb_bulb.led_RGB_setColor((255,255,255)) # white colour
        time.sleep(0.1)
        print(self.m_status)

    def motor_close(self):
        self.lcd.backlight(1)                       # turn off the lcd1602 backlight 
        self.lcd.lcd_clear()                        # clear the display
        self.mt7219.led_matrix(chr(0))              # clear matrix
        self.rgb_bulb.led_RGB_setColor((0,0,0))     # black colour
        time.sleep(0.1)
        self.servo.pwm.stop()                       # stop the servo

    ## Car direction triage
    def motor_triage(self,status):
        if status == 'Up/FF':
            self.motor_ff()
        elif status == 'Down/BK':
            self.motor_bk()
        elif status == 'Left/LF':
            self.motor_lf()
        elif status == 'Right/RT':
            self.motor_rt()
        elif status == 'Stop/SS':
            self.motor_ss()
    ## Car direction triage


def main():

    robot = Motor()
    time.sleep(3)
    for i in range(3):
        robot.motor_triage('Up/FF')
        time.sleep(1)
        robot.motor_triage('Down/BK')
        time.sleep(1)
        robot.motor_triage('Left/LF')
        time.sleep(1)
        robot.motor_triage('Right/RT')
        time.sleep(1)
        robot.motor_triage('Stop/SS')
        time.sleep(1)
    robot.motor_close()                             # turn off the motor display
    print('Finish!')

if __name__ == '__main__':

        try:
            main()
        except KeyboardInterrupt:
            pass
        finally:
            
            GPIO.cleanup()
