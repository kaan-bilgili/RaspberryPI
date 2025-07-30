import RPi.GPIO as GPIO
from time import sleep
inPIN= 40
outPIN=10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPIN,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(outPIN, GPIO.OUT)

valOld= 1
ledState = 0


try:
    while True:
        readVal= GPIO.input(inPIN)
        if readVal == 1 and valOld == 0:
            ledState = not ledState 
        GPIO.output(outPIN,ledState)
        valOld = readVal
        print(f"new value = {readVal} , old value = {valOld}")
        sleep(0.1)          
    
    
except KeyboardInterrupt :
    GPIO.cleanup()
    print("GPIO is free")
    
