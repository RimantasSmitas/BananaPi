import RPi.GPIO as GPIO
import time
import signal, os
import atexit

import sys
sys.path.insert(0, '/home/pi/robocar/MasterFolder')
import carEngine

sleeptimer = 0.005



def lineFollow():
    while True:
        print(carEngine.getSensorA(), carEngine.getSensorB(), carEngine.getSensorC())
        if carEngine.getSensorA()==1 and carEngine.getSensorB()==0 and carEngine.getSensorB()==0:
            carEngine.spinLeft()
            print("Spin Left")
        elif carEngine.getSensorA()==1 and carEngine.getSensorB()==1 and carEngine.getSensorC()==0:
            carEngine.left()
            print("Left")
        elif carEngine.getSensorA()==0 and carEngine.getSensorB()==0 and carEngine.getSensorC()==1:
            carEngine.spinRight()
            print("Spin Right")
        elif carEngine.getSensorA()==0 and carEngine.getSensorB()==1 and carEngine.getSensorC()==1:
            carEngine.right()
            print("Right")
        elif carEngine.getSensorA()==0 and carEngine.getSensorB()==1 and carEngine.getSensorC()==0:
            carEngine.forward()
            print("Forward")
        elif carEngine.getSensorA()==1 and carEngine.getSensorB()==1 and carEngine.getSensorC()==1:
            carEngine.forward()
            print("Forward")
        elif carEngine.getSensorA()==0 and carEngine.getSensorB()==0 and carEngine.getSensorC()==0:
            carEngine.backwardsBoth()
        time.sleep(sleeptimer)

lineFollow()
