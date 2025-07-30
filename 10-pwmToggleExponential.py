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


buttonIoldState=1
buttonDoldState=1
# we want a button with 10 steps and we want the incresement and decreasement exponential
# 1.585^10  = 100 so this number is gonna be our base value
baseValue = 1.585
step=0 

try:
    while True:
        myPwm.start(dutyCycle)
        buttonIstate=GPIO.input(37)
        buttonDstate=GPIO.input(35) 
        if buttonIstate == 1 and buttonIoldState == 0:
            if step <10:
                step+=1
            dutyCycle = int(baseValue ** step)
            if dutyCycle > 100:
                dutyCycle = 100
            myPwm.ChangeDutyCycle(dutyCycle)
        if buttonDstate == 1 and buttonDoldState == 0 :
            if step >=0:
                step-=1
            dutyCycle = int(baseValue ** step)
            myPwm.ChangeDutyCycle(dutyCycle)
        print(dutyCycle , "is the duty cycle")
        print(step,"is the step")
        buttonIoldState = buttonIstate
        buttonDoldState = buttonDstate
        
        time.sleep(0.1)
except KeyboardInterrupt :
    print("gpıo is free")
    GPIO.cleanup()

