import RPi.GPIO as GPIO
from time import sleep
import ADC0834
GPIO.setmode(GPIO.BCM)
pressPIN = 21
servoPIN = 20
ADC0834.setup()
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(pressPIN,GPIO.IN,pull_up_down = GPIO.PUD_UP)
servoPWM = GPIO.PWM(servoPIN , 50)
servoPWM.start(0)
lastDC = 0 
try :
    while True:
        yValue = ADC0834.getResult(0)
        servoDC = yValue * 10 / 255 + 2
            if abs(servoDC - lastDC) > 0.2:       # reduces the vibration of the servo 
            servoPWM.ChangeDutyCycle(servoDC)
            lastDC = servoDC
        print(yValue)
        sleep(0.2)
except KeyboardInterrupt:
    servoPWM.stop()
    print("GPIO is free")
    GPIO.cleanup()
