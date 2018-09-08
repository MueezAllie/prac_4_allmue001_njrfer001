import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if GPIO.input(7) == GPIO.HIGH:
        print("Reset Button was pressed.")
        time.sleep(0.3)

    if GPIO.input(11) == GPIO.HIGH:
        print("Frequency Button was pressed.")
        time.sleep(0.3)        
    
    if GPIO.input(13) == GPIO.HIGH:
        print("Start/Stop Button was pressed.")
        time.sleep(0.3)
        
    if GPIO.input(15) == GPIO.HIGH:
        print("Display button was pressed.")
        time.sleep(0.3)
        
        
GPIO.cleanup()
