import LCD1602
import time

LCD1602.init(0x27, 1)

try:
    while True:
        LCD1602.write(0, 0, 'serefli')
        LCD1602.write(0, 1, 'konti')
        time.sleep(0.5)   # çok hızlı spam atmasın
except KeyboardInterrupt:
    LCD1602.clear()
    print('Lcd is clear')
