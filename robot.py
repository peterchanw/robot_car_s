# Robot Car - main program
# Author: Peter Chan
# License: Public Domain
# June 2019

import sys
import time
import RPi.GPIO as GPIO
import motor as mv                  # import motor related modules

# import pynput related modules (keystroke detection)
from pynput import keyboard
### pynput detect key pressed
keyPress = ''

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format( key.char))
        global keyPress
        keyPress = key.char
    except AttributeError:
        print('special key {0} pressed'.format( key))
        if key == keyboard.Key.up:
            keyPress = keyboard.Key.up
        elif key == keyboard.Key.down:
            keyPress = keyboard.Key.down
        elif key == keyboard.Key.left:
            keyPress = keyboard.Key.left
        elif key == keyboard.Key.right:
            keyPress = keyboard.Key.right
        elif key == keyboard.Key.enter:
            keyPress = keyboard.Key.enter
        elif key == keyboard.Key.backspace:
            keyPress = keyboard.Key.backspace
        elif key == keyboard.Key.f8:
            keyPress = keyboard.Key.f8
        elif key == keyboard.Key.f9:
            keyPress = keyboard.Key.f9
        elif key == keyboard.Key.esc:
            keyPress = keyboard.Key.esc

def on_release(key):
    print('{0} released'.format( key))
    if key == keyboard.Key.esc:
        # Stop listener
        keyPress = keyboard.Key.esc
        return False

# in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
### pynput detect key pressed


def robot_init():      
    #set GPIO numbering mode and define output pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    global robot
    robot = mv.Motor()
    
## Main Robot Car function
def main():

    # Main program block

    global keyPress
    # Initialise robot
    robot_init()

    while True:
       robot.sonic.ultrasonic(robot)            # take measurement using HC-SR04 sensor
       # servo panning
       robot.servo.sv_st,robot.servo.sv_dir,robot.servo.sv_pan = robot.servo.servo_pan(robot.servo.sv_st,robot.servo.sv_dir,robot.servo.sv_pan)
       robot.adxl345.roll_car(robot)            # check the stability of car - accelerometer
       if keyPress == keyboard.Key.esc:
           break
       elif keyPress == 'w' or keyPress == keyboard.Key.up:     
           robot.motor_triage('Up/FF')
       elif keyPress == 'x' or keyPress == keyboard.Key.down:    
           robot.motor_triage('Down/BK')
       elif keyPress == 'a' or keyPress == keyboard.Key.left:      
           robot.motor_triage('Left/LF')
       elif keyPress == 'd' or keyPress == keyboard.Key.right:    
           robot.motor_triage('Right/RT')
       elif keyPress == 's' or keyPress == keyboard.Key.enter:
           robot.motor_triage('Stop/SS')
       elif keyPress == 'p':
           robot.servo.sv_pan = True                    # setup the flag for servo panning
       elif keyPress == 'o':
           robot.servo.servo_idle(robot)                # restore the servo panning
           keyPress = ''
       else:
           pass

## Main Robot Car function

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        robot.motor_close()
        listener.stop()
        GPIO.cleanup()

