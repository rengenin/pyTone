#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from waves import sinusoid

#Time to Frequency
wave1 = sinusoid(2.,1.,30000)
sin1 = wave1.sine_wave()

#sin_half = sin1[0:44099]

#FFT of sin1
ft1 = np.fft.fft(sin1)

mag1 = np.abs(ft1)

plt.subplot(3,1,1)
plt.plot(sin1)
#plt.xlim(0,8)

mag_filt_ind = np.where(mag1 == np.max(mag1)/2.)
mag_filt = mag1
#mag_filt[mag_filt_ind] = 0
print mag_filt_ind
#IFFT to get back to sin1
sin_ft = np.fft.ifft(ft1)


plt.subplot(3,1,2)
plt.plot(mag1)
plt.xlim(0,8)


plt.subplot(3,1,3)
plt.plot(sin_ft)

plt.show()