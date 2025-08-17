import RPi.GPIO as GPIO
import time
triggerPIN = 20
echoPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN , GPIO.OUT)
GPIO.setup(echoPIN , GPIO.IN)

try :
    while True:
        GPIO.output(triggerPIN,0)
        time.sleep(2E-6)
        GPIO.output(triggerPIN , 1 )
        time.sleep(10E-6)
        GPIO.output(triggerPIN,0)
        
        while GPIO.input(echoPIN) == 0:
            pass
        
        echoSTART = time.time()
        
        while GPIO.input(echoPIN) == 1:
            pass
        
        echoEND = time.time()
        
        totaltime= echoEND - echoSTART
        distance_cm =totaltime  * 34300 / 2

        time.sleep(0.3)
        print(distance_cm)
    
        
     
except KeyboardInterrupt:
    print("GPIO is free")
    GPIO.cleanup()