import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.OUT)
#GPIO.output(16, GPIO.LOW)

PWM = GPIO.PWM(16,50)
PWM.start(0)
DutyCycle = 0

while True:
    if GPIO.input(7) == GPIO.HIGH:
        print("Button 1 was pushed")
        DutyCycle = DutyCycle + 10
        PWM.ChangeDutyCycle(DutyCycle)
        time.sleep(0.3)
        if DutyCycle == 100:
            DutyCycle = 0
            PWM.ChangeDutyCycle(DutyCycle)

    if GPIO.input(11) == GPIO.HIGH:
        print("Button 2 was pushed")
        DutyCycle = DutyCycle - 14.285
        PWM.ChangeDutyCycle(DutyCycle)
        time.sleep(0.3) 
        if DutyCycle < 1:
            DutyCycle = 100
            PWM.ChangeDutyCycle(DutyCycle)        
    
    if GPIO.input(13) == GPIO.HIGH and DutyCycle>0:
        print("Button 3 was pushed")
        DutyCycle = 0
        PWM.ChangeDutyCycle(DutyCycle)
        time.sleep(0.3)
        
    elif GPIO.input(13) == GPIO.HIGH and DutyCycle==0:
        print("Button 3 was pushed")
        DutyCycle = 100
        PWM.ChangeDutyCycle(DutyCycle)
        time.sleep(0.3)
        
        
GPIO.cleanup()