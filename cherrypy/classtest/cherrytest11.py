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

	@cherrypy.expose
	def index(self):
		return index_html

	@cherrypy.expose
	def Forward(self):
		print ('Set both motors to move forward')
		SetMotorA(True)
		SetMotorB(True)
		return index_html
	@cherrypy.expose
	def Stop(self):
		print ('Set both motors to stop')
		SetMotorA(False)
		SetMotorB(False)
		return index_html
	@cherrypy.expose
	def Left(self):
		print ('Set 1 motor high, and 1 motor low')
		SetMotorA(False)
		SetMotorB(True)
		return index_html

	@cherrypy.expose
	def Right(self):
		print ('Set 1 motor high, and 1 motor low')
		SetMotorA(True)
		SetMotorB(False)
		return index_html

	@cherrypy.expose
	def Backwards(self):
		print ('Set both motors to run reverse')
		BothMotorsBackwards()
		return index_html

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(motorController())
