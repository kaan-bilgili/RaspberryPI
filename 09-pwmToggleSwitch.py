import RPi.GPIO as GPIO
import time
increaseButton=37
decreaseButton=35
ledGPIO= 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup([increaseButton ,decreaseButton],GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledGPIO,GPIO.OUT)

myPwm = GPIO.PWM(ledGPIO,50)
dutyCycle=0
myPwm.start(dutyCycle)

buttonIoldState=1
buttonDoldState=1


    
def increase(value):
    value+=20
    if value >= 100:
        value = 100
    return value

def decrease(value):
    value -= 20
    if value <= 0:
        value=0
    return value

try:
    while True:
        buttonIstate=GPIO.input(37)
        buttonDstate=GPIO.input(35) 
        if buttonIstate == 1 and buttonIoldState == 0:
            dutyCycle = increase(dutyCycle)
            myPwm.ChangeDutyCycle(dutyCycle)
        if buttonDstate == 1 and buttonDoldState == 0 :
            dutyCycle = decrease(dutyCycle)
            myPwm.ChangeDutyCycle(dutyCycle)
        print(dutyCycle)
        buttonIoldState = buttonIstate
        buttonDoldState = buttonDstate
        
        time.sleep(0.1)
except KeyboardInterrupt :
    print("gpıo is free")
    GPIO.cleanup()

