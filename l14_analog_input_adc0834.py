import RPi.GPIO as GPIO
from time import sleep
import ADC0834

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
try:
    while True:
        analogVal=ADC0834.getResult(1)  #The channel that you connected on the ADC
        print(analogVal)
        sleep(.2)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')