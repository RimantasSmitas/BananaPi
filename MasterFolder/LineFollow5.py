import RPi.GPIO as GPIO
import time
import signal, os
import atexit

import sys
sys.path.insert(0, '/home/pi/robocar/MasterFolder')
import carEngine

A = 13 # Right
B = 6 # Middle
C = 5 # Left

GPIO.setup(A, GPIO.IN)
GPIO.setup(B, GPIO.IN)
GPIO.setup(C, GPIO.IN)

def lineFollow():
    while True:
        print(GPIO.input(A), GPIO.input(B), GPIO.input(C))
        if GPIO.input(A)==1 and GPIO.input(B)==0 and GPIO.input(C)==0:
            carEngine.spinLeft()
            print("Spin Left")
        elif GPIO.input(A)==1 and GPIO.input(B)==1 and GPIO.input(C)==0:
            carEngine.Left()
            print("Left")
        elif GPIO.input(A)==0 and GPIO.input(B)==0 and GPIO.input(C)==1:
            carEngine.spinRight()
            print("Spin Right")
        elif GPIO.input(A)==0 and GPIO.input(B)==1 and GPIO.input(C)==1:
            carEngine.Right()
            print("Right")
        elif GPIO.input(A)==0 and GPIO.input(B)==1 and GPIO.input(C)==0:
            carEngine.Forward()
            print("Forward")
        elif GPIO.input(A)==1 and GPIO.input(B)==1 and GPIO.input(C)==1:
            carEngine.Forward()
            print("Forward")
        elif GPIO.input(A)==0 and GPIO.input(B)==0 and GPIO.input(C)==0:
            carEngine.BackwardsBoth()
        time.sleep(0.005)

lineFollow()
