import RPi.GPIO as GPIO
import time
import signal, os
import atexit
import sys
sys.path.insert(0, '/home/pi/robocar/MasterFolder')
import carEngine

# Fighting functions

defaultSpeed = 75
defaultLSpeed = defaultSpeed
defaultRSpeed = defaultSpeed - 2.4
turnSpeedDifferenceLight = 40
turnSpeedDifferenceHard = 25
spinSpeedMultiplication = 0.25

def escapeBack():
    print("Escaping to the back.")
    carEngine.backwardsBoth(defaultRSpeed, defaultLSpeed)
    time.sleep(0.3)
    carEngine.stop()

def charge():
    print("Charge forward")
    if sensorsFrontClean:
        carEngine.forward(defaultRSpeed + 10, defaultLSpeed + 10)
        time.sleep(0.005)
    else:
        escapeBack()

def sensorsFrontClean():
    if carEngine.getSensorA() == 0 and carEngine.getSensorB() == 0 and carEngine.getSensorC() == 0:
        return True
    return False

def aBitForward():
    for number in range(1, 10):
        if sensorsFrontClean:
            carEngine.forward(defaultRSpeed, defaultLSpeed)
        else:
            break

def sensorBackClean():
    if carEngine.getSensorD() == 0:
        return True
    return False

def lookForEnemy():
    range = carEngine.findEnemyDistance(0)
    if sensorsFrontClean() is False:
        print("Sensors FRONT are not clean, going back")
        escapeBack()
    elif sensorBackClean() is False:
        print("Sensors BACK are not clean, going front")
        aBitForward()
    else:
        if range > 60:
            print("Range is ", range, " spinning left.")
            carEngine.spinLeft(defaultRSpeed, defaultLSpeed, spinSpeedMultiplication)
        else:
            print("Range is ", range, "CHARGING.")
            charge()

while True:
    lookForEnemy()
    time.sleep(.05)
