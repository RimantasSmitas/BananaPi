import time
import datetime
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Echo = 20
Trig = 21
GPIO.setup(Echo,GPIO.OUT)
GPIO.setup(Trig,GPIO.IN)


def reading(sensor):
    pingtime = 0
    echotime = 0
    if sensor == 0:
        GPIO.output(Echo,GPIO.LOW)
        GPIO.output(Echo,GPIO.HIGH)
        pingtime=time.time()
        time.sleep(0.00001)
        GPIO.output(Echo,GPIO.LOW)
        while GPIO.input(Trig)==0:
            pingtime = time.time()
        while GPIO.input(Trig)==1:
            echotime=time.time()
        if (echotime is not None) and (pingtime is not None):
            elapsedtime = echotime - pingtime
            distance = elapsedtime * 17000
        else:
            distance = 0
#        print(pingtime)
#        print(echotime)
        return distance

while True:
    range = reading(0)
    print(range)
    time.sleep(0.25)

