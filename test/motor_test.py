import RPi.GPIO as GPIO          
from time import sleep

in1 = 18
in2 = 23
# enA = x
in3 = 24
in4 = 25
# enB = y

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

## GPIO.setup(enA,GPIO.OUT)
## GPIO.setup(enB,GPIO.OUT)
## p=GPIO.PWM(enA,1000)
## p.start(50)
## q=GPIO.PWM(enB,1000)
## q.start(50)

print("\n")
print("x-run s-stop f-forward b-backward l-left r-right esc-quit")
print("\n")    

while(1):
    x=input()
    if x=='x':
       print("run")
       if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
       else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in1,GPIO.HIGH)
         print("backward")
         x='z'
    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'
    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'
    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'
    elif x=='l':
        print("left")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        x='z'
    elif x=='r':
        print("right")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        x='z'
        
##    elif x=='a':
##        print("low")
##        p.ChangeDutyCycle(25)
##        q.ChangeDutyCycle(25)
##        x='z'
##    elif x=='m':
##        print("medium")
##        p.ChangeDutyCycle(50)
##        q.ChangeDutyCycle(50)
##        x='z'
##    elif x=='h':
##        print("high")
##        p.ChangeDutyCycle(100)
##        q.ChangeDutyCycle(100)
##        x='z'

    elif x==27:
        GPIO.cleanup()
        break
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
