import RPi.GPIO as GPIO
import time

# create a list of float number from 4.0 to 11.5 to maximise the servo swing
control = [x*0.5 for x in range(8, 25)]
servo = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)

# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)
# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%
# Since, 5% Duty Cycle of the PWM signal corresponds to extreme left position
# and 10% Duty Cycle corresponds to extreme right position, we need to vary the
# Duty Cycle between 5 and 10% to get a sweeping effect from the Servo Motor.

p=GPIO.PWM(servo,50)# 50hz frequency
p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )


try:
   while True:
      for x in range(16):
         p.ChangeDutyCycle(control[x])
         # time.sleep(0.03)
         time.sleep(0.5)
         print(x)
      for x in range(15,0,-1):
         p.ChangeDutyCycle(control[x])
         # time.sleep(0.03)
         time.sleep(0.5)
         print(x)
          
except KeyboardInterrupt:
       x = 9
       p.ChangeDutyCycle(control[x])
       time.sleep(0.5)
       GPIO.cleanup()
