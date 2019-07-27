'''
RGB led light - indicator lamp
Author: Peter Chan
License: GNU General Public Domain
Jul 2019
'''

import time
import RPi.GPIO as GPIO

## RGB coding
col_y = (255,255,0)     # yellow colour
col_g = (0,255,0)       # green colour
col_r = (255,0,0)       # red colour
col_b = (0,0,255)       # blue colour
col_m = (255,0,255)     # magenta colour
col_c = (0,255,255)     # cyan colour
col_w = (255,255,255)   # white colour
col_x = (0,0,0)         # black colour
col_o = (255,69,0)      # dark orange colour

class RGB_led:

    def __init__(self):
        self.pin_R = 17
        self.pin_G = 27
        self.pin_B = 22
        pins = {'pin_R':17, 'pin_G':27, 'pin_B':22} # pins is a dict
        GPIO.setmode(GPIO.BCM)                      # Numbers GPIOs by GPIO position
        for i in pins:
            GPIO.setup(pins[i], GPIO.OUT)           # Set pins' mode is output
            GPIO.output(pins[i], GPIO.HIGH)         # Set pins to high(+3.3V) to off led
        self.p_R = GPIO.PWM(self.pin_R, 2000)       # set Frequece to 2KHz
        self.p_G = GPIO.PWM(self.pin_G, 2000)
        self.p_B = GPIO.PWM(self.pin_B, 5000)
        self.p_R.start(0)                           # Initial duty Cycle = 0(leds off)
        self.p_G.start(0)
        self.p_B.start(0)

    def led_RGB_close(self):                        # Turn off RGB (i.e. PWM pins)
        self.p_R.stop()
        self.p_G.stop()
        self.p_B.stop() 

    def led_RGB_setColor(self,col_val):             # Set RGB led colour

        def map(x, in_min, in_max, out_min, out_max):   # cap the duty cycle value to 0-100
            return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

        r_duty = map(col_val[0], 0, 255, 100, 0)    # inverted logic
        g_duty = map(col_val[1], 0, 255, 100, 0)    # inverted logic
        b_duty= map(col_val[2], 0, 255, 100, 0)     # inverted logic  
        self.p_R.ChangeDutyCycle(r_duty)
        self.p_G.ChangeDutyCycle(g_duty)
        self.p_B.ChangeDutyCycle(b_duty)
        time.sleep(0.05)

def main():

    rgb = RGB_led()                                 # Create a RGB led object
    colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(255,255,255),(0,0,0)]
    for i in range(10):
        for color in colors:
            rgb.led_RGB_setColor(color)             # Change the RGB led colour
            time.sleep(0.5)
    rgb.led_RGB_close()


if __name__ == '__main__':

    try:
        main()
               
    except KeyboardInterrupt:
        pass
    
    finally:
        GPIO.cleanup()

