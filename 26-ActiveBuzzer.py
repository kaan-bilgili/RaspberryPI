import RPi.GPIO as GPIO
import time
buzzerPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPIN , GPIO.OUT)
try:
    while True:
        GPIO.output(buzzerPIN , 1)
        time.sleep(0.5)
        GPIO.output(buzzerPIN , 0)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO  is free")