import RPi.GPIO as GPIO
from time import sleep
import ADC0834

GPIO.setmode(GPIO.BCM)
ledPIN = 15
GPIO.setup(ledPIN,GPIO.OUT)
ADC0834.setup()
myPWM = GPIO.PWM(ledPIN , 50)
ledDC = 0
myPWM.start(ledDC)
try:
    while True:
        analogVal=ADC0834.getResult(1)  #The channel that you connected on the ADC
        print(analogVal)
        ledDC = 100 / 255 * analogVal   # since the potentiometer's range is 0 - 255 and the DC s range is 0 - 100
        myPWM.ChangeDutyCycle(ledDC)
        sleep(.2)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
