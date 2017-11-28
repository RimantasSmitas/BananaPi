import RPi.GPIO as GPIO
import time
import signal, os
import atexit

import sys
sys.path.insert(0, '/home/pi/robocar/MasterFolder')
import carEngine

sleeptimer = 0.004
defaultSpeed = 75
defaultLSpeed = defaultSpeed
defaultRSpeed = defaultSpeed -2.4
turnSpeedDifferenceLight = 50
turnSpeedDifferenceHard = 35
spinSpeedMultiplication = 0.15



def lineFollow():
    while True:
        print(carEngine.getSensorA(), carEngine.getSensorB(), carEngine.getSensorC())
        if carEngine.getSensorA()==1 and carEngine.getSensorB()==0 and carEngine.getSensorB()==0:
            carEngine.spinLeft(defaultRSpeed,defaultLSpeed,spinSpeedMultiplication)
            print("Spin Left")
        elif carEngine.getSensorA()==1 and carEngine.getSensorB()==1 and carEngine.getSensorC()==0:
            carEngine.left(defaultRSpeed,defaultLSpeed,turnSpeedDifferenceLight)
            print("Left")
        elif carEngine.getSensorA()==0 and carEngine.getSensorB()==0 and carEngine.getSensorC()==1:
            carEngine.spinRight(defaultRSpeed,defaultLSpeed,spinSpeedMultiplication)
            print("Spin Right")
        elif carEngine.getSensorA()==0 and carEngine.getSensorB()==1 and carEngine.getSensorC()==1:
            carEngine.right(defaultRSpeed, defaultLSpeed, turnSpeedDifferenceLight)
            print("Right")
        elif carEngine.getSensorA()==0 and carEngine.getSensorB()==1 and carEngine.getSensorC()==0:
            carEngine.forward(defaultRSpeed,defaultLSpeed)
            print("Forward")
        elif carEngine.getSensorA()==1 and carEngine.getSensorB()==1 and carEngine.getSensorC()==1:
            carEngine.forward(defaultRSpeed,defaultLSpeed)
            print("Forward")
        elif carEngine.getSensorA()==0 and carEngine.getSensorB()==0 and carEngine.getSensorC()==0:
            carEngine.backwardsBoth(defaultRSpeed - 10,defaultLSpeed - 10)
            print("Backward")
        time.sleep(sleeptimer)

lineFollow()
