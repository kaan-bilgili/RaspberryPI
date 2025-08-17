import RPi.GPIO as GPIO
import time

servoPIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  
p.start(0) 

time.sleep(2)  

try:
    while True:
        print("0 degrees")
        p.ChangeDutyCycle(2)
        time.sleep(0.75)
        p.ChangeDutyCycle(0)  # reduces vibration
        time.sleep(2)


        print("90 degrees")
        p.ChangeDutyCycle(7.5)
        time.sleep(0.75)
        p.ChangeDutyCycle(0)
        time.sleep(2)
        
        

        print("180 degrees")
        p.ChangeDutyCycle(12)
        time.sleep(0.75)
        p.ChangeDutyCycle(0)
        time.sleep(2)
        

except KeyboardInterrupt:
    print("GPIO is free")
    p.stop()
    GPIO.cleanup()
