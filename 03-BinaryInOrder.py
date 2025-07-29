import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
fifth=12
fourth=10
third= 15
second=13
first=11
GPIO.setup(fifth,GPIO.OUT)
GPIO.setup(fourth,GPIO.OUT)
GPIO.setup(third,GPIO.OUT)
GPIO.setup(second,GPIO.OUT)
GPIO.setup(first,GPIO.OUT)

GPIO.output(fifth,1) # 1
GPIO.output(fourth,0)
GPIO.output(third,0)
GPIO.output(second,0)
GPIO.output(first,0)
time.sleep(0.5)

GPIO.output(fifth,0)  #2
GPIO.output(fourth,1)
GPIO.output(third,0)
GPIO.output(second,0)
GPIO.output(first,0)
time.sleep(0.5)

GPIO.output(fifth,1)  #3
GPIO.output(fourth,1)
GPIO.output(third,0)
GPIO.output(second,0)
GPIO.output(first,0)
time.sleep(0.5)

GPIO.output(fifth,0) #4
GPIO.output(fourth,0)
GPIO.output(third,1)
GPIO.output(second,0)
GPIO.output(first,0)
time.sleep(0.5)

GPIO.output(fifth,1)  #5
GPIO.output(fourth,0)
GPIO.output(third,1)
GPIO.output(second,0)
GPIO.output(first,0)
time.sleep(0.5)

GPIO.output(fifth,0)  #6
GPIO.output(fourth,1)
GPIO.output(third,1)
GPIO.output(second,0)
GPIO.output(first,0)
time.sleep(0.5)

GPIO.output(fifth,1)  # 7
GPIO.output(fourth,1)
GPIO.output(third,1)
GPIO.output(second,0)
GPIO.output(first,0)
time.sleep(0.5)


GPIO.output(fifth,0)  # 8
GPIO.output(fourth,0)
GPIO.output(third,0)
GPIO.output(second,1)
GPIO.output(first,0)
time.sleep(0.5)


GPIO.output(fifth,1)  # 9
GPIO.output(fourth,0)
GPIO.output(third,0)
GPIO.output(second,1)
GPIO.output(first,0)
time.sleep(0.5)

GPIO.output(fifth,0)  #10
GPIO.output(fourth,1)
GPIO.output(third,0)
GPIO.output(second,1)
GPIO.output(first,0)
time.sleep(0.5)

GPIO.output(fifth,0)  #0
GPIO.output(fourth,0)
GPIO.output(third,0)
GPIO.output(second,0)
GPIO.output(first,0)
time.sleep(0.5)
GPIO.cleanup()

