import RPi.GPIO as GPIO
import time
import signal, os
import atexit

import sys
sys.path.insert(0, '/home/pi/robocar/MasterFolder')
import carEngine

# Fighting functions


def escapeBack():
    print("Escaping to the back.")
    carEngine.backwardsBoth()
    time.sleep(1)
    carEngine.stop()


def charge():
    print("Charge forward")
    if sensorsFrontClean:
        carEngine.forward()
        time.sleep(0.05)
    else:
        escapeBack()

# Checking the sensors around the car


def sensorsFrontClean():
    print(carEngine.getSensorA(), carEngine.getSensorB(), carEngine.getSensorC())
    if carEngine.getSensorA() == 0 and carEngine.getSensorB() == 0 and carEngine.getSensorC() == 0:
        return True
    return False


def sensorBackClean():
    if carEngine.getSensorD() == 0:
        return True
    return False


# main code

def lookForEnemy():
    range = carEngine.findEnemyDistance(0)
    if sensorsFrontClean() is False:
        escapeBack()
    elif sensorBackClean() is False:
        charge()
    else:
        if range > 50:
            carEngine.spinLeft()
        elif range < 50:
            charge()


#the actual code run
while True:
    lookForEnemy()
    time.sleep(.001)
