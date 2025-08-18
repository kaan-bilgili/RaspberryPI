class keypad:
    def __init__(self, rows = [17,27,22,5] ,
                 columns = [6,13,19,26] ,
                 labels = [
                        ['1','2','3','A'],
                        ['4','5','6','B'],
                        ['7','8','9','C'],
                        ['*','0','#','D']
                        ],
                 exitChar= "D"):
        self.rows = rows
        self.columns = columns
        self.labels=labels
        self.exitChar = exitChar
        
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        
        for r in rows:
            GPIO.setup(r,GPIO.OUT)
            GPIO.output(r,1)
    
        for c in columns:
            GPIO.setup(c,GPIO.IN , pull_up_down = GPIO.PUD_UP)
        
        
    def readKeypad(self):
         
        import RPi.GPIO as GPIO
        from datetime import datetime
        import time
        lastInput = ""
        last_pressed_time = datetime.now()
        returnVal=""
        key = True
        try:
            while key:
                for i,r in enumerate(self.rows):
                    time.sleep(0.001)
                    GPIO.output(r,0)
                    
                    for j, c in enumerate(self.columns):
                        if GPIO.input(c) == 0:
                            press_time = datetime.now()
                            if lastInput != self.labels[i][j] or  ( press_time - last_pressed_time ).total_seconds() > 0.107:
                                #print(( press_time - last_pressed_time ).total_seconds() is the seconds between strokes)
                                #print(f"{self.labels[i][j]} has pressed")
                                if self.labels[i][j] == self.exitChar:
                                    key = False
                                    return returnVal
                                    break
                                returnVal += (self.labels[i][j])
                                print(returnVal)
                            lastInput=self.labels[i][j]
                            last_pressed_time= datetime.now()
                            
                            time.sleep(0.1)
                    GPIO.output(r,1) 
        except KeyboardInterrupt:
            print("GPIO is free")
            
        finally :
            GPIO.cleanup()
        
    
mypad = keypad(exitChar = "A" )
print(mypad.readKeypad())
