import RPi.GPIO as GPIO
import time
import signal, os
import atexit

defaultLSpeed = 75
defaultRSpeed = 72.8
turnSpeedDifferenceLight = 11
turnSpeedDifferenceHard = 13

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

rightMotor = GPIO.PWM(PWMA, 50)
leftMotor = GPIO.PWM(PWMB, 50)
rightMotor.start(0)
leftMotor.start(0)

@atexit.register
def goodbye():
    GPIO.cleanup()

def DriveR(rightMotorSpeed):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    rightMotor.ChangeDutyCycle(rightMotorSpeed)

def DriveL(leftMotorSpeed):
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    leftMotor.ChangeDutyCycle(leftMotorSpeed)

def BackwardsR(rightMotorSpeed):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    rightMotor.ChangeDutyCycle(rightMotorSpeed)

def BackwardsL(leftMotorSpeed):
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    leftMotor.ChangeDutyCycle(leftMotorSpeed)

def Left():
    DriveR(defaultRSpeed+turnSpeedDifferenceLight)
    DriveL(defaultLSpeed - turnSpeedDifferenceLight)


def HardLeft():
    DriveR(defaultRSpeed+turnSpeedDifferenceHard)
    DriveL(defaultLSpeed - turnSpeedDifferenceHard)


def Right():
    DriveR(defaultRSpeed-turnSpeedDifferenceLight)
    DriveL(defaultLSpeed + turnSpeedDifferenceLight)


def HardRight():
    DriveR(defaultRSpeed-turnSpeedDifferenceHard)
    DriveL(defaultLSpeed + turnSpeedDifferenceHard)


def Forward():
    DriveR(defaultRSpeed)
    DriveL(defaultLSpeed)

def BackwardsBoth():
    BackwardsR(defaultRSpeed)
    BackwardsL(defaultLSpeed)

def Stop():
    print ('Calling  stop')
    DriveR(0)
    DriveL(0)


def spinLeft():
    BackwardsL(defaultLSpeed/3)
    DriveR(defaultRSpeed/3)

def spinRight():
    BackwardsR(defaultRSpeed/3)
    DriveL(defaultLSpeed/3)
