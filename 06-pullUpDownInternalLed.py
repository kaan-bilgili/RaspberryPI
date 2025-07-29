import RPi.GPIO as GPIO
import time
inPIN=40
outPIN=10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPIN,GPIO.OUT)
GPIO.setup(inPIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while True:
        value = GPIO.input(inPIN)
        if value == 0:
            GPIO.output(outPIN,1)
        else:
            GPIO.output(outPIN,0)
except KeyboardInterrupt :
    GPIO.cleanup()
    print("GPIO is free")