import RPi.GPIO as GPIO
import dht11
import time

GPIO.setmode(GPIO.BCM)

myDHT = dht11.DHT11(pin=21)

try:
    while True:
        result = myDHT.read()
        if result.is_valid():
            print('Temperature is:', result.temperature, '°C', 
                  'Humidity is:', result.humidity, '%')
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
