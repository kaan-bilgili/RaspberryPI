import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
redPIN = 37
greenPIN = 35
bluePIN = 33

redState = 0
greenState= 0
blueState=0


redBUT = 11
greenBUT = 13
blueBUT = 15


redBUTstateOld= 1
greenBUTstateOld=1
blueBUTstateOld=1



GPIO.setup([redPIN , greenPIN , bluePIN] , GPIO.OUT)
GPIO.setup([redBUT , greenBUT , blueBUT] , GPIO.IN , pull_up_down = GPIO.PUD_UP)

try:
    while True:
        redBUTstate = GPIO.input(redBUT)
        greenBUTstate= GPIO.input(greenBUT)
        blueBUTstate = GPIO.input(blueBUT)
        
        if redBUTstate == 1 and redBUTstateOld == 0:
            redState = not redState
        
        if greenBUTstate == 1 and greenBUTstateOld == 0:
            greenState = not greenState
            
        if blueBUTstate == 1 and blueBUTstateOld == 0:
            blueState = not blueState
            
        redBUTstateOld = redBUTstate
        greenBUTstateOld = greenBUTstate
        blueBUTstateOld = blueBUTstate
        
        GPIO.output(redPIN, redState)
        GPIO.output(greenPIN, greenState)
        GPIO.output(bluePIN, blueState)
        sleep(0.1)
        
        
    
except KeyboardInterrupt :
    print("GPIO is free")
    GPIO.cleanup()

 