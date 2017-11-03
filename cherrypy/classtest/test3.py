import signal, os
import RPi.GPIO as GPIO
import time


AIN1 = 17
AIN2 = 27
PWMA = 2
BIN1 = 10
BIN2 = 22
PWMB = 3


# Pin for linesensor:  							 
A = 6 		#left
B = 13 		#middle
C = 5   #right

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(A, GPIO.IN) # sensor set as input
GPIO.setup(B, GPIO.IN)
GPIO.setup(C, GPIO.IN)
GPIO.setwarnings(False)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT) 
GPIO.setup(PWMB, GPIO.OUT)

rightmotor = GPIO.PWM(PWMA, 50)  # channel=12 frequency=50Hz
rightmotor.start(0)

def handler(signum, frame):  #stop when ctrl-c is recieved
    print ('Signal handler called with signal', signum)
    print ('exiting')
    GPIO.output(PWMA, GPIO.LOW)
    GPIO.cleanup()
    exit(0)

# When recieving ctrl-C
signal.signal(signal.SIGINT, handler)


rightmotor = GPIO.PWM(PWMA, 50)
leftmotor = GPIO.PWM(PWMB, 50)

def backward():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(PWMA, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    GPIO.output(PWMB, GPIO.HIGH)


def forward():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(PWMA, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    GPIO.output(PWMB, GPIO.HIGH)


def right():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(PWMA, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    GPIO.output(PWMB, GPIO.HIGH)


def left():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(PWMA, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    GPIO.output(PWMB, GPIO.HIGH)


def stop():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(PWMA, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    GO.output(PWMB, GPIO.LOW)
    rightmotor.ChangeDutyCycle(0)
    leftmotor.ChangeDutyCycle(0)

def check(A,B,C):
 while True:
  if B==0 and A==1 and C==1:
    forward()
  elif A==0:
    left()
  elif C==0:
    right()
  elif A==0 and B==0 and C==0:
    stop()


forward()


