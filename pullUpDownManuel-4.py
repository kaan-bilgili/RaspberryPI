import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
inPIN=10
GPIO.setup(inPIN,GPIO.IN)
#pull up circiut with a button

try:
    while True:
        value = GPIO.input(inPIN)
        print(f"The value is {value}")
        sleep(0.3)
        if value == 0:
            print("Pressed the button")
except KeyboardInterrupt :
        print("GPIO has cleaned")
        GPIO.cleanup()
