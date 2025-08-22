from keypad import Keypad
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO


mypad = Keypad(exitChar="A")
text = mypad.readKeypad()

rsPIN = 18
enablePIN = 23
d4PIN = 21
d5PIN = 20
d6PIN = 16
d7PIN = 12

GPIO.setmode(GPIO.BCM)
lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16, rows=2,
    pin_rs=rsPIN,
    pin_e=enablePIN,
    pins_data=[d4PIN, d5PIN, d6PIN, d7PIN]
)

 LCD
lcd.clear()
line1 = text[:16] if text else ""
line2 = text[16:32] if len(text) > 16 else ""
lcd.write_string(line1)
lcd.cursor_pos = (1, 0)
lcd.write_string(line2)
