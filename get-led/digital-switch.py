import RPi.GPIO as GPIO
import time
state=0

GPIO.setmode(GPIO.BCM)
but = 13
GPIO.setup(but, GPIO.IN)
led = 26
GPIO.setup(led, GPIO.OUT)
while True:
    if GPIO.input(but):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)