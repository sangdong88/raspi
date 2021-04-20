import RPi.GPIO as GPIO
import time

LED = 18
SW = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial = False)
GPIO.setup(SW, GPIO.IN, GPIO.PUD_UP)

while True:
    keyin = GPIO.input(SW)
    if keyin == 0:
        GPIO.output(LED, True)
        print("Push")
    else :
        GPIO.output(LED, False)
        print("Not push")

GPIO.cleanup()