#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from waves import sinusoid, square_wave, saw_tooth, wave_math

#Time to Frequency
wave1 = sinusoid(2.,1.,False)
sin1 = wave1.sine_wave()

#FFT of sin1
ft1 = np.fft.rfft(sin1)

#IFFT to get back to sin1
sin_ft = np.fft.irfft(ft1)

#freq = np.zeroes(22051)
#freq[11025] = 

print ft1[11025]

plt.subplot(3,1,1)
plt.plot(sin1)

plt.subplot(3,1,2)
plt.plot(np.abs(ft1))
plt.xlim(0,4)

plt.subplot(3,1,3)
plt.plot(sin_ft)

#plt.show()