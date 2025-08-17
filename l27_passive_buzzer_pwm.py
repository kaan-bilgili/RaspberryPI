import RPi.GPIO as GPIO
import time
buzzerPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPIN , GPIO.OUT)
myPwm = GPIO.PWM(buzzerPIN,440)
dutyCycle = 0
myPwm.start(dutyCycle)

try:
    while True:
        for i in range(1,30):
            myPwm.ChangeDutyCycle(i)  # volume up-down
            time.sleep(.2)
            
        for i in range(30,1,-1):
            myPwm.ChangeDutyCycle(i)
            time.sleep(.2)
            
        for freq in range(440, 1000, 10):  
            myPwm.ChangeFrequency(freq)   # frequency of the sound
            time.sleep(0.05)
        
        for freq in range(1000, 440, -10):  
            myPwm.ChangeFrequency(freq)
            time.sleep(0.05)

except KeyboardInterrupt:
    print("GPIO is free")
    GPIO.cleanup()
