#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from waves import sinusoid, wave_add, wave_diff

wavfile = read('signal.wav')
signal = wavfile[1]#time domain function
sample_rate = wavfile[0]#sampling rate from the wave file

filt = sinusoid(50,1,30000)
sin_filt = filt.sine_wave()

filtered = wave_diff(signal,sin_filt)

plt.subplot(211)
plt.plot(signal)

plt.subplot(212)
plt.plot(filtered)

plt.show()