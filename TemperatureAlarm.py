import time
import w1thermsensor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
tmax = 29.0
tmin = 2.0
sensor = w1thermsensor.W1ThermSensor()

import time
logs = open('logs.txt', 'w')
for i in range (0,60):
    temp=sensor.get_temperature()
    if temp > tmax:
        GPIO.output(21, GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)
        print("HOT")
        logs.write('HOT!')
    elif temp < tmin:
        GPIO.output(21, GPIO.LOW)
        GPIO.output(17, GPIO.HIGH)
        print("ICE ALERT")
        logs.write('ICE ALERT')
    else:
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        
    tempera=str(temp)
    timer=time.localtime()
    h=str(timer[3])
    m=str(timer[4])
    s=str(timer[5])
    logs.write(tempera)
    print(tempera, end="")
    logs.write('    ')
    print('    ', end="")
    if int(h)<10:
     logs.write('0'+h)
     print('0'+h, end="")
    else:
     logs.write(h)
     print(h, end="")
    logs.write(':')
    print(':', end="")
    if int(m)<10:
     logs.write('0'+m)
     print('0'+m, end="")
    else:
     logs.write(m)
     print(m, end="")
    logs.write(':')
    print(':', end="")
    if int(s)<10:
     logs.write('0'+s)
     print('0'+s, end="")
    else:
     logs.write(s)
     print(s, end="")
    logs.write('\n')
    print('\n')
    time.sleep(1)

logs.close()
GPIO.output(21, GPIO.HIGH)
GPIO.output(26, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
