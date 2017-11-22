import RPi.GPIO as GPIO
import time
import signal, os
import atexit

## The speed settings for the linefollow ex.
defaultSpeed = 75
defaultLSpeed = defaultSpeed
defaultRSpeed = defaultSpeed - 2.2
turnSpeedDifferenceLight = 11
turnSpeedDifferenceHard = 13
spinSpeedMultiplication = 0.3
#


#Setting variables for pins.
PWMA = 2
PWMB = 3
AIN1 = 17
AIN2 = 27
BIN1 = 22
BIN2 = 10

#Setting up pins for motors. Making a pin cleanup in case there are settings left from previous program.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

#Creating motor variables
rightMotor = GPIO.PWM(PWMA, 50)
leftMotor = GPIO.PWM(PWMB, 50)
rightMotor.start(0)
leftMotor.start(0)



#DriveFunctions
def driveR(rightMotorSpeed):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    rightMotor.ChangeDutyCycle(rightMotorSpeed)

def driveL(leftMotorSpeed):
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    leftMotor.ChangeDutyCycle(leftMotorSpeed)

def backwardsR(rightMotorSpeed):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    rightMotor.ChangeDutyCycle(rightMotorSpeed)

def backwardsL(leftMotorSpeed):
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    leftMotor.ChangeDutyCycle(leftMotorSpeed)

def left():
    driveR(defaultRSpeed+turnSpeedDifferenceLight)
    driveL(defaultLSpeed - turnSpeedDifferenceLight)

def hardLeft():
    driveR(defaultRSpeed+turnSpeedDifferenceHard)
    driveL(defaultLSpeed - turnSpeedDifferenceHard)

def right():
    driveR(defaultRSpeed-turnSpeedDifferenceLight)
    driveL(defaultLSpeed + turnSpeedDifferenceLight)

def hardRight():
    driveR(defaultRSpeed-turnSpeedDifferenceHard)
    driveL(defaultLSpeed + turnSpeedDifferenceHard)

def forward():
    driveR(defaultRSpeed)
    driveL(defaultLSpeed)

def backwardsBoth():
    backwardsR(defaultRSpeed)
    backwardsL(defaultLSpeed)

def stop():
    print ('Calling  stop')
    driveR(0)
    driveL(0)

def spinLeft():
    backwardsL(defaultLSpeed*spinSpeedMultiplication)
    driveR(defaultRSpeed*spinSpeedMultiplication)

def spinRight():
    backwardsR(defaultRSpeed*spinSpeedMultiplication)
    driveL(defaultLSpeed*spinSpeedMultiplication)

#sensors
#sensor on the right

#Setting variables and pins for sensors
A = 13 # Right
B = 6 # Middle
C = 5 # Left
GPIO.setup(A, GPIO.IN)
GPIO.setup(B, GPIO.IN)
GPIO.setup(C, GPIO.IN)

def getSensorA():
    return GPIO.input(A)

#sensor the middle
def getSensorB():
    b = GPIO.input(B)
    return  b
    print(b)
#sensor on the left
def getSensorC():
    c = GPIO.input(C)
    return c
    print(c)
def getSonar():
    return

@atexit.register
def goodbye():
    GPIO.cleanup()
