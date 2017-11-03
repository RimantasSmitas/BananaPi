
import RPi.GPIO as GPIO
import time

# Pin Definitons:
IRsensor1 = 7 # Broadcom pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(IRsensor1, GPIO.IN) # sensor set as input 

# PROGRAM
while True:
        A = GPIO.input(IRsensor1)
        print (A)
        time.sleep(0.01)
