import RPi.GPIO as GPIO
import dht11
import time

import LCD1602
LCD1602.init(0x27, 1)

buttonPIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
myDHT = dht11.DHT11(pin=21)

buttonLastValue = 1
current = True


try:
    while True:
        readVal = GPIO.input(buttonPIN)
        if readVal == 1 and buttonLastValue == 0:
            current = not current
            LCD1602.clear()
        buttonLastValue = readVal
        
        
        
        result = myDHT.read()
        if result.is_valid() and current:
            LCD1602.write(0, 0, 'Temp : '+ str(result.temperature)+ " °C")            
            LCD1602.write(0, 1, 'Humidity : '+str(result.humidity) + "%")
            print('Temperature is:', result.temperature, '°C', 
                  'Humidity is:', result.humidity, '%')
            time.sleep(0.2)
        elif result.is_valid() :
            tF = result.temperature * 9/5 + 32
            h = result.humidity
            LCD1602.write(0, 0, f"Temp : {tF:.1f}F")
            LCD1602.write(0, 1, f"Humidity : {h:.1f}%")
            print('Temperature is:', tF, '°F', 
                  'Humidity is:', h, '%')


            time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
