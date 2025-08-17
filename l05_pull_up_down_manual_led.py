import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
inPIN=40
outPIN= 10
GPIO.setup(outPIN,GPIO.OUT)
GPIO.setup(inPIN,GPIO.IN)
#pull up circiut with a button

try:
    while True:
        value = GPIO.input(inPIN)
        print(f"The value is {value}")
        sleep(0.1)
        if value == 0:
            GPIO.output(outPIN,1)
        else:
             GPIO.output(outPIN,0)
except KeyboardInterrupt :
        print("GPIO has cleaned")
        GPIO.cleanup()
