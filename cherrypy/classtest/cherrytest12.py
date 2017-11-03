class motorController:
	@cherrypy.expose
        def SetMotorA(motorShouldRun):
                if(motorShouldRun):
                        GPIO.output(AIN1, GPIO.HIGH)
                        GPIO.output(AIN2, GPIO.LOW)
                        GPIO.output(PWMA, GPIO.HIGH)
                else:
                        GPIO.output(PWMA, GPIO.LOW)
                print('Set motor A to: ', motorShouldRun)

	@cherrypy.expose
        def SetMotorB(motorShouldRun):
                if(motorShouldRun):
                        GPIO.output(BIN1, GPIO.HIGH)
                        GPIO.output(BIN2, GPIO.LOW)
                        GPIO.output(PWMB, GPIO.HIGH)
                else:
                        GPIO.output(PWMB, GPIO.LOW)
                print('Set motor B to: ', motorShouldRun)

	@cherrypy.expose
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


