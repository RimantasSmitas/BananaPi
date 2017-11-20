import RPi.GPIO as GPIO
import time
import signal, os
import atexit

defaultLSpeed = 50
defaultRSpeed = 47.8
defaulTurnSpeedO = 50
defaulTurnSpeedI = 30

PWMA = 2
PWMB = 3

AIN1 = 17
AIN2 = 27
BIN1 = 22
BIN2 = 10

#Pins for sensors
A = 13 # Right
B = 6 # Middle
C = 5 # Left


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(A, GPIO.IN)
GPIO.setup(B, GPIO.IN)
GPIO.setup(C, GPIO.IN)

rightmotor = GPIO.PWM(PWMA, 50)
rightmotor.start(0)
leftmotor = GPIO.PWM(PWMB, 50)
leftmotor.start(0)


@atexit.register
def goodbye():
    GPIO.cleanup()

def setMotorA(motorSpeed):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    rightmotor.ChangeDutyCycle(motorSpeed)

def setMotorB(motorSpeed):
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    leftmotor.ChangeDutyCycle(motorSpeed)

def setMotorABackwards(motorSpeed):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    rightmotor.ChangeDutyCycle(motorSpeed)

def setMotorBBackwards(motorSpeed):
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    leftmotor.ChangeDutyCycle(motorSpeed)

def Forward(motorASpeed,motorBSpeed):
    print("Calling forward")
    setMotorA(motorASpeed)
    setMotorB(motorBSpeed)

def Stop():
    print ('Calling  stop')
    setMotorA(0)
    setMotorB(0)

def Right():
    Forward(70,55)
    print ('Turning right')
    setMotorABackwards(True)
    setMotorB(True)

def Left():
    Forward(55,70)
    print ('Turning left')

def Backwards():
    print ('Set both motors to run reverse')
    setMotorABackwards(defaultLSpeed)
    setMotorBBackwards(defaultRSpeed)

def lineFollow():
    while True:
        print(GPIO.input(A), GPIO.input(B), GPIO.input(C))
        if GPIO.input(A)==1 and GPIO.input(B)==0 and GPIO.input(C)==0:
            Left()
        elif GPIO.input(A)==1 and GPIO.input(B)==1 and GPIO.input(C)==0:
            Left()
        elif GPIO.input(A)==0 and GPIO.input(B)==0 and GPIO.input(C)==1:
            Right()
        elif GPIO.input(A)==0 and GPIO.input(B)==1 and GPIO.input(C)==1:
            Right()
        elif GPIO.input(A)==0 and GPIO.input(B)==1 and GPIO.input(C)==0:
            Forward(defaultRSpeed,defaultLSpeed)
        elif GPIO.input(A)==1 and GPIO.input(B)==1 and GPIO.input(C)==1:
            Forward(defaultRSpeed,defaultRSpeed)
        elif GPIO.input(A)==0 and GPIO.input(B)==0 and GPIO.input(C)==0:
            Backwards()
            time.sleep(0.1)

lineFollow()
