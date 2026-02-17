from r2r import R2R_DAC
import signal_generator as sg
import time
amplitude = 3
sampl_fq = 1000
freq = 10
gpio_bits=[16,20,21,25,2,17,27,22]
dynamic_range=3.183
dac = None
try: 
    dac = R2R_DAC(gpio_bits, dynamic_range, verbose=True)

    t0 = time.time()

    while True:
        t = time.time() - t0
        a_norm = sg.get_sin_wave(freq, t)
        voltage = amplitude * a_norm
        dac.set_voltage(voltage)
        sg.wait_f_p(sampl_fq)
finally:
        if dac is not None:
            dac.deinit()