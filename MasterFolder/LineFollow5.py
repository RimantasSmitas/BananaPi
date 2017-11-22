import RPi.GPIO as GPIO
import time
import signal, os
import atexit

import sys
sys.path.insert(0, '/home/pi/robocar/MasterFolder')
import carEngine

SLEEPTIMER = 0.005



GPIO.setup(A, GPIO.IN)
GPIO.setup(B, GPIO.IN)
GPIO.setup(C, GPIO.IN)

def lineFollow():
    while True:
        print(GPIO.input(A), GPIO.input(B), GPIO.input(C))
        if carEngine.getSensorA==1 and carEngine.getSensorB==0 and carEngine.getSensorB==0:
            carEngine.spinLeft()
            print("Spin Left")
        elif carEngine.getSensorA==1 and carEngine.getSensorB==1 and carEngine.getSensorC==0:
            carEngine.Left()
            print("Left")
        elif carEngine.getSensorA==0 and carEngine.getSensorB==0 and carEngine.getSensorC==1:
            carEngine.spinRight()
            print("Spin Right")
        elif carEngine.getSensorA==0 and carEngine.getSensorB==1 and carEngine.getSensorC==1:
            carEngine.Right()
            print("Right")
        elif carEngine.getSensorA==0 and carEngine.getSensorB==1 and carEngine.getSensorC==0:
            carEngine.Forward()
            print("Forward")
        elif carEngine.getSensorA==1 and carEngine.getSensorB==1 and carEngine.getSensorC==1:
            carEngine.Forward()
            print("Forward")
        elif carEngine.getSensorA==0 and carEngine.getSensorB==0 and carEngine.getSensorC==0:
            carEngine.BackwardsBoth()
        time.sleep(SLEEPTIMER)

lineFollow()
