import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 60) # channel 18 , 50 Hz
print("HEllo python")
p.start(0)
a = 1
aa = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40,30 ,20, 10, 0)
while a <= 3:
    print("Cycle :",  a)
    for i in aa:
        p.ChangeDutyCycle(i)
        time.sleep(0.2)
        print(i)
    for dc in range(0,101,10):
        p.ChangeDutyCycle(dc)
        time.sleep(0.5)
        print(dc)
    for dc2 in range(100,-1,-10):
        p.ChangeDutyCycle(dc2)
        time.sleep(0.5)
        print(dc2)
    a = a +1

p.stop()
GPIO.cleanup()