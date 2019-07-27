'''
Ultrasonic device detect barrier and move around
Author: Peter Chan
License: GNU General Public Domain
Jul 2019
'''

import time
import RPi.GPIO as GPIO                 # import GPIO related modules
import motor as mv                      # import motor related modules
import hc_sr04 as sonic                 # import HC-SR04 related modules

class Sonic_dev:

    def __init__(self):
        self.device = sonic.Sonic()     # create HC-SR04 object to measure
        
    ## detect distance with repeat readings
    def detect_dist(self,no):
        d = [0]*no
        for x in range(no):
            d[x] = self.device.distance()
            time.sleep(0.05)
        dt = int (sum(d)/len(d))
        return dt
    ## detect distance with repeat readings
         
    ## Ultrasonic HC-SR04 coding
    def ultrasonic(self,motor):
    
        dt = self.detect_dist(5)                    # detect barrier distance
        motor.p_rgb = motor.rgb_status
        motor.p_status = motor.m_status
        # detect bypass
        if dt < 30:
            # detect bypass
            motor.rgb_bulb.led_RGB_setColor((255,69,0))     # dark orange
            time.sleep(0.05)
            motor.motor_ss()                        # stop the car first
            # moving and discover obstacle
            if motor.p_status != 'Stop/SS' and motor.p_status != 'Init/IN':   
                motor.motor_triage('Down/BK')       # turn back
                time.sleep(0.05)
                motor.motor_triage('Stop/SS')
                motor.servo.pwm.ChangeDutyCycle(motor.servo.control[8])   # servo to 90 degree
                time.sleep(0.1)
                while True:
                    motor.servo.pwm.ChangeDutyCycle(motor.servo.control[0]) # check left-hand side for barrier  
                    time.sleep(0.1)
                    dt = self.detect_dist(5)            # detect barrier distance
                    if dt > 30:                         # Check left-hand side clear
                        motor.motor_triage('Left/LF')
                        time.sleep(0.01)
                        print('LF', motor.p_status)
                        break
                    else: 
                        motor.servo.pwm.ChangeDutyCycle(motor.servo.control[17])  # right left-hand side for barrier  
                        time.sleep(0.2)
                        dt = self.detect_dist(5)        # detect barrier distance
                        if dt > 30:                     # Check right-hand side clear
                            motor.motor_triage('Right/RT')
                            time.sleep(0.01)
                            print('RT', motor.p_status)
                            break
                        else:
                            motor.servo.pwm.ChangeDutyCycle(motor.servo.control[8])   # restore servo to 90 degree
                            time.sleep(0.2)
                            motor.motor_triage('Down/BK')  # turn back further
                            time.sleep(0.05)
                            motor.motor_triage('Stop/SS')
                            print('BK', motor.p_status)
                motor.servo.pwm.ChangeDutyCycle(motor.servo.control[8])  # restore servo to 90 degree
                time.sleep(0.1)
            print('Restore', motor.p_status)
            motor.motor_triage(motor.p_status)              # restore original direction
            motor.m_status = motor.p_status
            motor.rgb_status = motor.p_rgb
        motor.rgb_bulb.led_RGB_setColor(motor.p_rgb)        # restore original colour      
        if dt > 300:
            dist = '<>'
        else:
            dist = str(dt)
        msg = "Dist: " + dist + " cm     "
        motor.lcd.lcd_display_string(msg,2)
        time.sleep(0.05)

def main():

    global robot
    robot = mv.Motor()
    time.sleep(3)
    robot.motor_triage('Up/FF')
    while True:
        robot.sonic.ultrasonic(robot)
   
    
if __name__ == '__main__':

        try:
            main()
        except KeyboardInterrupt:
            pass
        finally:
            robot.motor_close()
            GPIO.cleanup()



