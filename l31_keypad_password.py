# This project is a simple Python script that allows a Raspberry Pi to read input from a 4x4 matrix keypad using the RPi.GPIO library. 
# The rows are configured as outputs and the columns as inputs with pull-up resistors, and the program continuously scans the keypad to detect pressed keys and print their values. 
# A basic debounce mechanism using datetime ensures more stable detection and the script exits cleanly with GPIO cleanup when interrupted, making it useful for projects such as PIN entry, security systems, or menu navigation.


import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
rows = [17,27,22,5]
columns = [6,13,19,26]

KEYS = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]



for r in rows:
    GPIO.setup(r,GPIO.OUT)
    GPIO.output(r,1)
    
for c in columns:
    GPIO.setup(c,GPIO.IN , pull_up_down = GPIO.PUD_UP)
def keypad():   
    lastInput = ""
    last_pressed_time = datetime.now()
    returnVal=""
    key = True
    try:
        while key:
            for i,r in enumerate(rows):
                time.sleep(0.001)
                GPIO.output(r,0)
                
                for j, c in enumerate(columns):
                    if GPIO.input(c) == 0:
                        press_time = datetime.now()
                        if lastInput != KEYS[i][j] or  ( press_time - last_pressed_time ).total_seconds() > 0.107:
                            #print(( press_time - last_pressed_time ).total_seconds())
                            print(f"{KEYS[i][j]} has pressed")
                            if KEYS[i][j] == "D":
                                key = False
                                return returnVal
                                break
                            returnVal += (KEYS[i][j])
                        lastInput=KEYS[i][j]
                        last_pressed_time= datetime.now()
                        
                        time.sleep(0.1)
                GPIO.output(r,1) 
    except KeyboardInterrupt:
        print(returnVal)
        print("GPIO is free")
        GPIO.cleanup()
        
    finally :
        print(returnVal)

password = input("write your password\t")
while True:
    print("use keypad to write the password")
    keypadReturn = keypad()
    if keypadReturn == password :
        print("logging in ...")
        break
    else:
        print("Wrong password")
        time.sleep(0.4)



