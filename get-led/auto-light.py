import RPi.GPIO as GPIO
import time
state=0

GPIO.setmode(GPIO.BCM)
but = 6
GPIO.setup(but, GPIO.IN)
led = 26
GPIO.setup(led, GPIO.OUT)
while True:
    state = GPIO.input(but)
    if state == 1:
        GPIO.output(led, 0)
    else:
        GPIO.output(led, 1)