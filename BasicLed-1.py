import RPi.GPIO as GPIO
import time
inPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin,GPIO.OUT)
try:
    GPIO.output(inPin,True)
    time.sleep(1)
    GPIO.output(inPin,False)
    
except KeyboardInterrupt:
    
    GPIO.cleanup()
