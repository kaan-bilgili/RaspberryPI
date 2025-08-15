#When the light level falls below a set threshold (dark environment) and the PIR sensor detects motion, the buzzer beeps in short intervals.

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

import ADC0834

#buzzer
buzzerPIN = 14
GPIO.setup(buzzerPIN , GPIO.OUT)

#photoresistor
ADC0834.setup()
threshold = 185

#pir
pirPIN = 21
GPIO.setup(pirPIN,GPIO.IN)
time.sleep(10)

try:
    while True:
        time.sleep(0.1)
        lightVal=ADC0834.getResult(0)  #The channel that you connected on the ADC
        print(f"Ligth value is {lightVal}")
        
        if lightVal < threshold:    
            print("Lights off")
        
            pirvalue = GPIO.input(pirPIN)
            print(pirvalue)
            if pirvalue == 1 :
                print("Object in sight")
                
                GPIO.output(buzzerPIN , 1)
                time.sleep(0.5)
                GPIO.output(buzzerPIN , 0)
                time.sleep(0.5)
                
            else :
                print("Stable")
            time.sleep(0.1)
        
        
    
except KeyboardInterrupt :
    print("GPIO is free")
    GPIO.cleanup()
    