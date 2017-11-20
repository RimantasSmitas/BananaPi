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


@atexit.register
def goodbye():
	GPIO.cleanup()

#def handler(signum, frame):
#	print("Signal handler called with signal ", signum)
#	print("existing")
#	GPIO.output(PWMA, GPIO.LOW)
#	GPIO.output(PWBA, GPIO.LOW)
#	GPIO.cleanup()
#	exit(0))

#signal.signal(signal.SIGINT, handler)

def SetMotorA(motorShouldRun):
	if(motorShouldRun):
		GPIO.output(AIN1, GPIO.HIGH)
		GPIO.output(AIN2, GPIO.LOW)
		GPIO.output(PWMA, GPIO.HIGH)
	else:
		GPIO.output(PWMA, GPIO.LOW)
		print('Set motor A to: ', motorShouldRun)

def SetMotorB(motorShouldRun):
	if(motorShouldRun):
		GPIO.output(BIN1, GPIO.HIGH)
		GPIO.output(BIN2, GPIO.LOW)
		GPIO.output(PWMB, GPIO.HIGH)
	else:
		GPIO.output(PWMB, GPIO.LOW)
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
	print ('Set both motors to stop')
	SetMotorA(False)
	SetMotorB(False)

def Right():
	print ('Set 1 motor high, and 1 motor low')
	SetMotorA(False)
	SetMotorB(True)

def Left():
	print ('Set 1 motor high, and 1 motor low')
	SetMotorA(True)
	SetMotorB(False)

def Backwards():
	print ('Set both motors to run reverse')
	BothMotorsBackwards()

def lineFollow():

#	while True:
#		print('A', GPIO.input(A), ' B', GPIO.input(B), ' C', GPIO.input(C))
#		time.sleep(.500)



	while True:
		if GPIO.input(A)== 1 and GPIO.input(B)==0 and GPIO.input(C)==0:
			Left()
		elif GPIO.input(A)==1 and GPIO.input(B)==1 and GPIO.input(C)==0:
			Left()
		elif GPIO.input(A)== 0 and GPIO.input(B)==0 and GPIO.input(C)==1:
			Right()
		elif GPIO.input(A)==0 and GPIO.input(B)==1 and GPIO.input(C)==1:
			Right()
		elif GPIO.input(A)==0 and GPIO.input(B)==1 and GPIO.input(C)==0:
			Forward()
		elif GPIO.input(A)==1 and GPIO.input(B)==1 and GPIO.input(C)==1:
			Forward()
		elif GPIO.input(A)==0 and GPIO.input(B)==0 and GPIO.input(C)==0:
			Backwards()
		time.sleep(.100)
lineFollow()
