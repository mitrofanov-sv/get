import RPi.GPIO as GPIO
import time
state=0
period=1.0

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)

while True:
    state = not state
    GPIO.output(led, state)
    time.sleep(period)
    
