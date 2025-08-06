# pip3 install RPLCD
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from time import sleep

rsPIN = 18        
enablePIN = 23    
d4PIN = 13       
d5PIN = 6         
d6PIN = 5         
d7PIN = 15        

GPIO.setmode(GPIO.BCM)

lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16, rows=2,
    pin_rs=rsPIN,
    pin_e=enablePIN,
    pins_data=[d4PIN, d5PIN, d6PIN, d7PIN]
)


lcd.clear()
lcd.write_string("1234567345678878")
lcd.cursor_pos = (1, 0)
lcd.write_string("abcdemnosadasd")

    