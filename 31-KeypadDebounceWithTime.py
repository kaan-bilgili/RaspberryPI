# Introduces a Python script to read input from a 4x4 matrix keypad using RPi.GPIO
# Implements row/column scanning, basic debounce logic with datetime,
# clean GPIO cleanup on exit. Useful for PIN entry, security, or menu navigation projects.


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
    
lastInput = ""
last_pressed_time = datetime.now()
try:
    while True:
        for i,r in enumerate(rows):
            time.sleep(0.001)
            GPIO.output(r,0)
            
            for j, c in enumerate(columns):
                if GPIO.input(c) == 0:
                    press_time = datetime.now()
                    if lastInput != KEYS[i][j] or  ( press_time - last_pressed_time ).total_seconds() > 0.107:
                        print(( press_time - last_pressed_time ).total_seconds())
                        print(f"{KEYS[i][j]} has pressed")
                    lastInput=KEYS[i][j]
                    last_pressed_time= datetime.now()
                    
                    time.sleep(0.1)
            GPIO.output(r,1)
except KeyboardInterrupt:
    print("GPIO is free")
    GPIO.cleanup()


