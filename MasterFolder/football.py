import cherrypy
import RPi.GPIO as GPIO
import time
import signal, os
import atexit

import sys
sys.path.insert(0, '/home/pi/robocar/MasterFolder')
import carEngine

file = open('/home/pi/robocar/MasterFolder/webinterface.html')
index_html = file.read()
file.close()

PWMA = 2
PWMB = 3

AIN1 = 17
AIN2 = 27
BIN1 = 22
BIN2 = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)


@atexit.register
def goodbye():
    GPIO.cleanup()


@cherrypy.expose
def index(self):
    return index_html


@cherrypy.expose
def forward(self):
    carEngine.Forward()
    return index_html


@cherrypy.expose
def stop(self):
    carEngine.stop()
    return index_html


@cherrypy.expose
def right(self):
    carEngine.right()
    return index_html


@cherrypy.expose
def left(self):
    carEngine.left()
    return index_html


@cherrypy.expose
def bothBackward(self):
    carEngine.bothBackward()
    return index_html


cherrypy.server.socket_host = '0.0.0.0'