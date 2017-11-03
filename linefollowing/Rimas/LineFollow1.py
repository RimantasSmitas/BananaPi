import RPi.GPIO as GPIO
import time
import signal, os
import atexit


@atexit.register
def goodbye():
        GPIO.cleanup()



PWMA = 2
PWMB = 3

AIN1 = 17
AIN2 = 27
BIN1 = 22
BIN2 = 10

#Pins for sensors
A = 13 #Right
B = 6 #Middle
C = 5 #Left

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(PWMA, GPIO.OUT)
motorA = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
motorA.start(0)
motorA.ChangeDutyCycle(50)

GPIO.setup(PWMB, GPIO.OUT)
motorB = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
motorB.start(0)
motorB.ChangeDutyCycle(50)

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(A, GPIO.IN)
GPIO.setup(B, GPIO.IN)
GPIO.setup(C, GPIO.IN)

def SetMotorA(motorShouldRun):
    if (motorShouldRun):
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        motorA.ChangeDutyCycle(50)
       # GPIO.output(PWMA, GPIO.HIGH) #///////////////////////////////////////
    else:

      #@  GPIO.output(PWMA, GPIO.LOW)
        print('Set motor A to: ', motorShouldRun)

def SetMotorB(motorShouldRun):
        if (motorShouldRun):
            GPIO.output(BIN1, GPIO.HIGH)
            GPIO.output(BIN2, GPIO.LOW)
            motorB.ChangeDutyCycle(50)
        #   GPIO.output(PWMB, GPIO.HIGH)
        else:
      #      GPIO.output(PWMB, GPIO.LOW)
            print('Set motor B to: ', motorShouldRun)

def BothMotorsBackwards():
        #Reversing the GPIO direction for backwards flow.
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        GPIO.output(PWMB, GPIO.HIGH)
        GPIO.output(PWMA, GPIO.HIGH)

def Forward():
        print("Set both motors to move forward")
        SetMotorA(True)
        SetMotorB(True)

def Stop():
    print('Set both motors to stop')
    SetMotorA(False)
    SetMotorB(False)

def Right():
    print('Set 1 motor high, and 1 motor low')
    motorB.ChangeDutyCycle(70)
    motorA.ChangeDutyCycle(50)
 #   SetMotorA(True)
 #   SetMotorB(True)

def Left():
    print ('Set 1 motor high, and 1 motor low')

    motorB.ChangeDutyCycle(50)
    motorA.ChangeDutyCycle(70)

#    SetMotorA(True)
 #   SetMotorB(True)

def Backwards():
    print ('Set both motors to run reverse')
    BothMotorsBackwards()


def lineFollow():
    while True:
        if GPIO.input(A) == 1 and GPIO.input(B) == 0 and GPIO.input(C) == 0:
            Left()
        elif GPIO.input(A) == 1 and GPIO.input(B) == 1 and GPIO.input(C) == 0:
            Left()
        elif GPIO.input(A) == 0 and GPIO.input(B) == 0 and GPIO.input(C) ==1:
            Right()
        elif GPIO.input(A) == 0 and GPIO.input(B) == 1 and GPIO.input(C) == 1:
            Right()
        elif GPIO.input(A) == 0 and GPIO.input(B) == 1 and GPIO.input(C) == 0:
            Forward()
        elif GPIO.input(A) == 1 and GPIO.input(B) == 1 and GPIO.input(C) == 1:
            Forward()
        elif GPIO.input(A) == 0 and GPIO.input(B) == 0 and GPIO.input(C) == 0:
            Backwards()


lineFollow()
