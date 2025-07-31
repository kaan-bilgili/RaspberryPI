import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
redPIN = 37
greenPIN = 35
bluePIN = 33
GPIO.setup([redPIN , greenPIN , bluePIN] , GPIO.OUT)
GPIO.output(redPIN , 1 )
GPIO.output(bluePIN , 1 )
GPIO.output(greenPIN , 1 )
sleep(5)
GPIO.output(redPIN , 0 )
GPIO.output(bluePIN , 0 )
GPIO.output(greenPIN , 0 )
GPIO.cleanup()
