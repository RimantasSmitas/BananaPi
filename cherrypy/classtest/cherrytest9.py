#!/usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy
import RPi.GPIO as GPIO

file = open('/home/pi/cherrypy/classtest/htmlfile2.html')
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


class motorController:

    @cherrypy.expose
    def index(self):
        return index_html

    @cherrypy.expose
    def Forward(self):
        print("Called forward")

	#motor A
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(PWMA, GPIO.HIGH)

	#motor B
        GPIO.output(BIN1, GPIO.HIGH)
        GPIO.output(BIN2, GPIO.LOW)
        GPIO.output(PWMB, GPIO.HIGH)
        return index_html

    @cherrypy.expose
    def Stop(self):
	print("Called stop")
	GPIO.output(PWMA, GPIO.LOW)
	GPIO.output(PWMB, GPIO.LOW)
	return index_html

    @cherrypy.expose
    def Left(self):
	print("Called left")
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(PWMA, GPIO.HIGH)
        return index_html

    @cherrypy.expose
    def Right(self):
	print("Called right")
        GPIO.output(BIN1, GPIO.HIGH)
        GPIO.output(BIN2, GPIO.LOW)
        GPIO.output(PWMB, GPIO.HIGH)
        return index_html

    @cherrypy.expose
    def Backwards(self):
	print("Called backwards)
	#motor A
	GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(PWMA, GPIO.LOW)

	#motor B
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        GPIO.output(PWMB, GPIO.LOW)
        return index_html

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(motorController())
