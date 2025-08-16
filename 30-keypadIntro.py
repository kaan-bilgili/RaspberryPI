#A simple Python script to read a 4x4 matrix keypad with Raspberry Pi using RPi.GPIO.
#Rows are set as outputs, columns as inputs with pull-ups.
#The program scans rows, detects pressed keys, and prints the corresponding value.

import RPi.GPIO as GPIO
import time
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
try:
    while True:
        for i,r in enumerate(rows):
            time.sleep(0.001)
            GPIO.output(r,0)
            
            for j, c in enumerate(columns):
                if GPIO.input(c) == 0:
                    print("BUTTON HAS PRESSED")
                    if lastInput != KEYS[i][j]:
                        print(f"{KEYS[i][j]} has pressed")
                    lastInput=KEYS[i][j]
                    
                    time.sleep(0.4)
            GPIO.output(r,1)
except KeyboardInterrupt:
    print("GPIO is free")
    GPIO.cleanup()
