import datetime
import time
import math
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)
tr=0
s1=0
s2=0
fl=1
while True:
        
    i = GPIO.input(18)
    
    if i==1 :
        print("BLINK ON")
        if fl==1:
          s1=time.time()
          print(s1)
          tr=1
          fl=0
    elif i==0 and fl==0:
        print("BLINK OFF")
        if tr==1:
            s2=time.time()
            print("dif=")        
            print(s2-s1)
            tr=0
            fl=1
            #time.sleep(1)
        
        
GPIO.cleanup()
