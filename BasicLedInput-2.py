import RPi.GPIO as GPIO
import time
inPin= 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin,GPIO.OUT)

cont ="y"
while cont == "y":
    number = int(input("How many blink do you want? \n"))
    for i in range(number):
        GPIO.output(inPin,True)
        time.sleep(1)
        GPIO.output(inPin,False)
        time.sleep(1)
    cont = input("Would you like to continue ?\n"
                    "Press Y to continue\n"
                     "Something else to exit\n").lower()  
GPIO.cleanup()