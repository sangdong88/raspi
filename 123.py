import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED = GPIO.setup(18, GPIO.OUT)

print("HEllo python")
a = 0
while a <= 10:
    GPIO.output(18, True)
    time.sleep(3)
    GPIO.output(18, False)
    time.sleep(1)
    a = a +1
    print(a)

GPIO.cleanup()