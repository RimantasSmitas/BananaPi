import RPi.GPIO as GPIO
import time
import signal, os
import atexit

## The speed settings for the linefollow ex.
defaultSpeed = 75
defaultLSpeed = defaultSpeed -1.5
defaultRSpeed = defaultSpeed
turnSpeedDifferenceLight = 15
turnSpeedDifferenceHard = 25
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

# defyning sonar variables
sonarIn = 21
sonarOut = 20
GPIO.setup(sonarOut,GPIO.OUT)
GPIO.setup(sonarIn,GPIO.IN)

# Sonar function


def findEnemyDistance(sensor):
    pingtime = 0
    echotime = 0
    if sensor == 0:
        GPIO.output(sonarOut,GPIO.LOW)
        GPIO.output(sonarOut,GPIO.HIGH)
        pingtime=time.time()
        time.sleep(0.00001)
        GPIO.output(sonarOut,GPIO.LOW)
        while GPIO.input(sonarIn)==0:
            pingtime = time.time()
        while GPIO.input(sonarIn)==1:
            echotime=time.time()
        if (echotime is not None) and (pingtime is not None):
            elapsedtime = echotime - pingtime
            distance = elapsedtime * 17000
        else:
            distance = 0
        print(pingtime)
        print(echotime)
        return distance

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

# sensors
# sensor on the right

# Setting variables and pins for sensors
A = 13 # Right
B = 6 # Middle
C = 5 # Left
D = 19 # Back

GPIO.setup(A, GPIO.IN)
GPIO.setup(B, GPIO.IN)
GPIO.setup(C, GPIO.IN)
GPIO.setup(D, GPIO.IN)


def getSensorA():
    return GPIO.input(A)


def getSensorB():
    return GPIO.input(B)


def getSensorC():
    return GPIO.input(C)


def getSensorD():
    return GPIO.input(D)


def getSonar():
    return


@atexit.register
def goodbye():
    GPIO.cleanup()
