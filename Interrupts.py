#Defining the interrupts and their applications
GPIO.add_event_detect(RESET, GPIO.RISING, callback = Reset, bouncetime = 200)

GPIO.add_event_detect(FREQ, GPIO.RISING, callback = changeFreq, bouncetime = 300)

GPIO.add_event_detect(STARTSTOP, GPIO.RISING, callback = Stop, bouncetime = 300)

GPIO.add_event_detect(DISP, GPIO.RISING, callback = Display, bouncetime = 300)

#Removing interrupts
GPIO.remove_event_detect(RESET)
GPIO.remove_event_detect(FREQ)
GPIO.remove_event_detect(STOP)
GPIO.remove_event_detect(DISP)
