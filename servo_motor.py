'''
Servo motor panning
Author: Peter Chan
License: GNU General Public Domain
Jul 2019
'''

import time
import RPi.GPIO as GPIO
import motor as mv

class Servo:

    def __init__(self):
        ## Servo Motor coding   
        self.servo_pin = 5
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin,GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin,50)      # 50hz frequency
        # In Servo Motor:
        # 1ms pulse for 0 degree (LEFT)
        # 1.5ms pulse for 90 degree (MIDDLE)
        # 2ms pulse for 180 degree (RIGHT)
        # so for 50hz, one frequency is 20ms
        # duty cycle for 0 degree = (1/20)*100 = 5% (0.05 x 20ms = 1ms)
        # duty cycle for 90 degree = (1.5/20)*100 = 7.5% (0.075 x 20ms = 1.5ms)
        # duty cycle for 180 degree = (2/20)*100 = 10% (0.1 x 20ms = 1ms)
        # Since, 5% Duty Cycle of the PWM signal corresponds to extreme left position
        # and 10% Duty Cycle corresponds to extreme right position, we need to vary the
        # Duty Cycle between 5 and 10% to get a sweeping effect from the Servo Motor.
        # calibrate Duty Cycle from 6 to 12 for 0 degree to 180 degree
        # create a list of float number to maximise the servo swing
        self.control = [(12-5)/(180-0)*x + 5.0 for x in range(0,180,15)]
        self.pwm.start(6)                       # starting duty cycle (it set the servo to 90 degree )
        self.sv_st =  6                         # Servo idle position
        self.sv_dir = 1                         # Servo panning direction
        self.sv_pan = False                     # Servo panning flag
        self.pwm.ChangeDutyCycle(self.control[6]) # reset the servo motor to 90 degree
        time.sleep(0.5)   

    def servo_pan(self,sv_status,sv_direction,sv_panning):
        if sv_panning:                # Servo panning
           print(sv_status)
           self.pwm.ChangeDutyCycle(self.control[sv_status])
           # time.sleep(0.03)     
           time.sleep(0.5)
           if sv_status < 11 and sv_direction == 1:
              sv_status += 1          # count up
           elif sv_status > 0 and sv_direction == -1:
              sv_status -= 1          # count down
           elif sv_status == 11 and sv_direction == 1:
              sv_direction = -1       # reverse
              sv_status -= 1          # count down
           elif sv_status == 0 and sv_direction == -1:
              sv_direction = 1        # increment
              sv_status += 1          # count up
        else:
           sv_status = 0              # Servo panning setup 
           sv_direction = 1
        return sv_status,sv_direction,sv_panning

    def servo_idle(self,robot):
        self.sv_st =  6                                     # Servo idle position
        self.sv_dir = 1                                     # Servo panning direction
        self.sv_pan = False                                 # Servo panning flag
        robot.rgb_bulb.led_RGB_setColor((255,69,0))         # dark orange
        time.sleep(0.05)
        robot.rgb_bulb.led_RGB_setColor(robot.rgb_status)   # restore original colour
        self.pwm.ChangeDutyCycle(self.control[6])           # reset the servo motor to 90 degree
        time.sleep(0.5)

## Servo Motor coding

def main():
    global robot
    robot = mv.Motor()
    sv_status = 0
    sv_direction = 1
    sv_panning = True
    while True:
        sv_status,sv_direction,sv_panning = robot.servo.servo_pan(sv_status,sv_direction,sv_panning)
        print ('count:', sv_status)
        print ('Direction: ', sv_direction)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        robot.servo.servo_idle(robot)
        robot.servo.pwm.stop()
        GPIO.cleanup()
