import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
inPIN = 21
GPIO.setup(inPIN , GPIO.IN)
sleep(15) # that is needed for pir motion sensor to get ready to use

try:
    while True:
        motion = GPIO.input(inPIN)
        print(motion)
        sleep(0.1)
    
except KeyboardInterrupt:
    print("GPIO is free to use")
    GPIO.cleanup()

