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
    backwardsBoth()
    time.sleep(1)
    stop()


def charge():
    print("Charge forward")
    for number in range(1, 20):
        if sensorsFrontClean:
            forward()
            time.sleep(0.05)
        else:
            escapeBack()

# Checking the sensors around the car


def sensorsFrontClean():
    print(GPIO.input(A), GPIO.input(B), GPIO.input(C))
    if GPIO.input(A) == 0 and GPIO.input(B) == 0 and GPIO.input(C) == 0:
        return True
    return False


def sensorBackClean():
    if GPIO.input(D) == 0:
        return True
    return False


# main code

def lookForEnemy():
    range = findEnemyDistance(0)
    if sensorsFrontClean() == False:
        escapeBack()
    elif sensorBackClean() == False:
        charge()
    else:
        if range > 50:
            left()
        elif range < 50:
            charge()


#the actual code run
while True:
    lookForEnemy()
    time.sleep(.001)
