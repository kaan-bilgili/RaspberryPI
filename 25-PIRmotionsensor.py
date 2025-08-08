import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
inPIN = 21
GPIO.setup(inPIN,GPIO.IN)
time.sleep(10)
try:
    while True:
        value = GPIO.input(inPIN)
        print(value)
        if value == 1 :
            print("Object in sight")
        else :
            print("Stable")
        time.sleep(0.1)
    
except KeyboardInterrupt :
    print("GPIO is free")
    GPIO.cleanup()
    