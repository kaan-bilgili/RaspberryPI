import RPi.GPIO as GPIO
import time
outPIN=37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPIN , GPIO.OUT)
#pwm stands  for oulse width modulation and allows us to simulate analog output voltages
# pins give 3.3v as their high value
myPWM=GPIO.PWM(outPIN,50)   # 50 is the frequency
myPWM.start(80)# that value is the duty cycle as a percentage. %x  100 max
time.sleep(5)

myPWM.ChangeDutyCycle(5)
myPWM.ChangeFrequency(10)
time.sleep(5)

myPWM.stop()

GPIO.cleanup()