import RPi.GPIO as GPIO
import time
state=0

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty += 1.0
    if duty > 100.0:
        duty=0.0

import time
from adc_plot import plot_voltage_vs_time
from r2r_adc import R2R_ADC 

DYNAMIC_RANGE = 3.3 
COMPARE_TIME = 0.0001 
DURATION = 3.0  

def main():
    adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, 
                  compare_time=COMPARE_TIME, 
                  verbose=False)
    
    voltage_values = []
    time_values = []
    
    try:
        start_time = time.time()
        while time.time() - start_time < DURATION:
            voltage = adc.get_sc_voltage()
            current_time = time.time() - start_time
            
            voltage_values.append(voltage)
            time_values.append(current_time)

        plot_voltage_vs_time(time_values, voltage_values, DYNAMIC_RANGE)
        
    finally:
        del adc

if __name__ == "__main__":
    main()
