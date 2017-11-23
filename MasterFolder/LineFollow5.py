import RPi.GPIO as GPIO
import time
import signal, os
import atexit

import sys
sys.path.insert(0, '/home/pi/robocar/MasterFolder')
import carEngine

sleeptimer = 0.002
defaultSpeed = 85
defaultLSpeed = defaultSpeed -1.5
defaultRSpeed = defaultSpeed
turnSpeedDifferenceLight = 40
turnSpeedDifferenceHard = 25
spinSpeedMultiplication = 0.25



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
            carEngine.backwardsBoth(defaultRSpeed,defaultLSpeed)
        time.sleep(sleeptimer)

lineFollow()
