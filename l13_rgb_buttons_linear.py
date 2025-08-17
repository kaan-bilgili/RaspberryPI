import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
redPIN = 37
greenPIN = 35
bluePIN = 33

redDC = 0
greenDC= 0
blueDC=0

redBUT = 11
greenBUT = 13
blueBUT = 15

redBUTstateOld= 1
greenBUTstateOld=1
blueBUTstateOld=1

GPIO.setup([redPIN , greenPIN , bluePIN] , GPIO.OUT)
GPIO.setup([redBUT , greenBUT , blueBUT] , GPIO.IN , pull_up_down = GPIO.PUD_UP)

redPWM = GPIO.PWM(redPIN,50)
greenPWM = GPIO.PWM(greenPIN,50)
bluePWM = GPIO.PWM(bluePIN,50)

redPWM.start(redDC)
greenPWM.start(greenDC)
bluePWM.start(blueDC)

try:
    while True:
        redBUTstate = GPIO.input(redBUT)
        greenBUTstate = GPIO.input(greenBUT)
        blueBUTstate = GPIO.input(blueBUT)
        
        if redBUTstate == 1 and redBUTstateOld== 0 :
            redDC += 25
            if redDC > 100:
                redDC = 0
        
        if greenBUTstate == 1 and greenBUTstateOld == 0 :
            greenDC += 25
            if greenDC > 100:
                greenDC = 0 
            
        if blueBUTstate == 1 and blueBUTstateOld == 0 :
            blueDC += 25
            if blueDC > 100:
                blueDC = 0
        
        redPWM.ChangeDutyCycle(redDC)
        greenPWM.ChangeDutyCycle(greenDC)
        bluePWM.ChangeDutyCycle(blueDC)
        print ( redDC , greenDC , blueDC)
        
                
        redBUTstateOld = redBUTstate
        greenBUTstateOld = greenBUTstate
        blueBUTstateOld = blueBUTstate
        
        sleep(0.1)
    
except KeyboardInterrupt :
    print("GPIO good to go")
    GPIO.cleanup()
