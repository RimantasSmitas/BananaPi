import RPi.GPIO as GPIO
import time
import signal, os
import atexit


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

def setMotorA(motorShouldRun):
    if (motorShouldRun):
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        rightmotor.ChangeDutyCycle(67.8)
    else:
        GPIO.output(PWMA, GPIO.LOW)

def setMotorABackwards(motorShouldRun):
    if (motorShouldRun):
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        rightmotor.ChangeDutyCycle(47.8)
    else:
        GPIO.output(PWMA, GPIO.LOW)


def setMotorB(motorShouldRun):
    if (motorShouldRun):
        GPIO.output(BIN1, GPIO.HIGH)
        GPIO.output(BIN2, GPIO.LOW)
        leftmotor.ChangeDutyCycle(70)
    else:
        GPIO.output(PWMB, GPIO.LOW)


def setMotorBBackwards(motorShouldRun):
    if (motorShouldRun):
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        leftmotor.ChangeDutyCycle(50)
    else:
        GPIO.output(PWMB, GPIO.LOW)

def Forward():
	print("Calling forward")
	setMotorA(True)
	setMotorB(True)


def Stop():
	print ('Calling  stop')
	setMotorA(False)
	setMotorB(False)

def Right():
	Forward()
	print ('Turning right')
	leftmotor.ChangeDutyCycle(70)
	rightmotor.ChangeDutyCycle(55)
	setMotorABackwards(True)
	setMotorB(True)

def Left():
	Forward()
	print ('Turning left')
	leftmotor.ChangeDutyCycle(55)
	rightmotor.ChangeDutyCycle(70)
	setMotorA(True)
	setMotorBBackwards(True)

def Backwards():
	print ('Set both motors to run reverse')
	setMotorABackwards(True)
	setMotorBBackwards(True)

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
			Forward()
		elif GPIO.input(A)==1 and GPIO.input(B)==1 and GPIO.input(C)==1:
			Forward()
		elif GPIO.input(A)==0 and GPIO.input(B)==0 and GPIO.input(C)==0:
			Backwards()
		time.sleep(0.1)

lineFollow()
