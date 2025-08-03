import RPi.GPIO as GPIO
from time import sleep
import ADC0834
GPIO.setmode(GPIO.BCM)
pressPIN = 21
ADC0834.setup()
GPIO.setup(pressPIN,GPIO.IN,pull_up_down = GPIO.PUD_UP)
try :
    while True:
        xValue = ADC0834.getResult(1)
        yValue = ADC0834.getResult(0)
        value = GPIO.input(pressPIN)
        print(xValue , yValue , value)
        sleep(0.2)
except KeyboardInterrupt:
    print("GPIO is free")
    GPIO.cleanup()
