import RPi.GPIO as GPIO
from time import sleep
import ADC0834

GPIO.setmode(GPIO.BCM)
redPIN = 15
greenPIN =14
bluePIN = 22
GPIO.setup([redPIN,greenPIN,bluePIN],GPIO.OUT)
ADC0834.setup()
myPWMred = GPIO.PWM(redPIN , 50)
myPWMgreen = GPIO.PWM(greenPIN , 50)
myPWMblue = GPIO.PWM(bluePIN , 50)
redDC = 0
greenDC = 0
blueDC = 0

myPWMred.start(redDC)
myPWMgreen.start(greenDC)
myPWMblue.start(blueDC)

try :
    while True:
        redVal = ADC0834.getResult(0)
        redDC = 100/255 * redVal
        myPWMred.ChangeDutyCycle(redDC)
        
        greenVal = ADC0834.getResult(1)
        greenDC = 100/255 * greenVal
        myPWMgreen.ChangeDutyCycle(greenDC)
        
        blueVal = ADC0834.getResult(2)
        blueDC = 100/255 * blueVal
        myPWMblue.ChangeDutyCycle(blueDC)
        sleep(.2)
        
    
    
except KeyboardInterrupt :
    print("GPIO is free")
    GPIO.cleanup()
    
    