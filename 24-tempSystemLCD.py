import RPi.GPIO as GPIO
import dht11
import RPLCD
import time
from RPLCD.gpio import CharLCD
GPIO.setmode(GPIO.BCM)

#for the dht11
myDHT = dht11.DHT11(pin=21)

#for lcd setup
rsPIN = 18        
enablePIN = 23    
d4PIN = 13       
d5PIN = 6         
d6PIN = 5         
d7PIN = 15        

lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16, rows=2,
    pin_rs=rsPIN,
    pin_e=enablePIN,
    pins_data=[d4PIN, d5PIN, d6PIN, d7PIN]
)

try:
    while True:
        result = myDHT.read()
        if result.is_valid():
            print('Temperature is:', result.temperature, '°C', 
                  'Humidity is:', result.humidity, '%')
            
            lcd.clear()
            lcd.cursor_pos = (0, 8)
            lcd.write_string(f"{result.temperature}°C")
           
            lcd.cursor_pos = (1, 8)
            lcd.write_string(f"{result.humidity}%")

        
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')

