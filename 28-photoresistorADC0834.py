import RPi.GPIO as GPIO
import time
import ADC0834
GPIO.setmode(GPIO.BCM)

ADC0834.setup()

try:
    while True:
        time.sleep(0.1)
        analogVal=ADC0834.getResult(0)  #The channel that you connected on the ADC
        print(f"Ligth value is {analogVal}")
        
    
    
except KeyboardInterrupt:
    print("GPIO IS FREE")
    GPIO.cleanup()


