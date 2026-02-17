import numpy as np
import time

def get_sin_wave(freq, t):
    return (np.sin(2 * np.pi * freq * t) + 1) / 2
def wait_f_p(sampl_fq):
    period = 1.0 / sampl_fq
    time.sleep(period)