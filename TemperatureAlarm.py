import time
import w1thermsensor
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.output(21, GPIO.HIGH)
GPIO.output(26,GPIO.LOW)
GPIO.output(17,GPIO.LOW)

class DefaultValues:
    def __init__(self):
        self.tmax = 29.0
        self.tmin = 2.0
        self.sensor = w1thermsensor.W1ThermSensor()
        
class DateWithTime:
    def __init__(self):
        self.now = datetime.now()
        self.dateTime = self.now.strftime("%m/%d/%Y %H:%M:%S")

with open('logs.txt', 'w') as logs:
 for i in range (0,10):#60):
    dv=DefaultValues()
    temp=dv.sensor.get_temperature()
    if temp > dv.tmax:
        GPIO.output(21, GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)
        print("HOT")
        logs.write('HOT!')
    elif temp < dv.tmin:
        GPIO.output(21, GPIO.LOW)
        GPIO.output(17, GPIO.HIGH)
        print("ICE ALERT")
        logs.write('ICE ALERT')
    else:
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        
    temper=str(temp)
    dwt = DateWithTime()
    mess = dwt.dateTime
    
    logs.write(mess+" "+temper+'\n')
    print(mess,temper, end="\n")
    time.sleep(1)

GPIO.output(21, GPIO.HIGH)
GPIO.output(26, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
