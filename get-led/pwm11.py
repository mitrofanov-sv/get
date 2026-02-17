import RPi.GPIO as GPIO 

class PWM_DAC:
    def __init__(self,gpio_pin,pwn_frequency,dynamic_range,verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwn_frequency = pwn_frequency

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin,GPIO.OUT,initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_pin,0)
        GPIO.cleanup()

    def set_voltage(self,voltage):
        dynamic_voltage = float(3.11)
        if not ( 0.0 <= voltage <= dynamic_voltage):
            print(f"Напряжение выходит за данимический диапозон ЦАП (0.00 - {dynamic_voltage: .2f} 2B)")
            print("устанавливаем 0.0В")
            return 0
        return int((voltage / dynamic_voltage) * 255)


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12,1200,3.290,True)
        pwm = GPIO.PWM(dac.gpio_pin,200)
        duty=0
        pwm.start(duty)
        while True:
            try:
                voltage = float (input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

                print(dac.set_voltage(voltage))
                duty = dac.set_voltage(voltage)*100/255
                pwm.ChangeDutyCycle(duty)
            except ValueError:
                print("Не число")
    finally:
        dac.deinit()
