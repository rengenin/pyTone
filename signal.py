#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from waves import sinusoid, square_wave, saw_tooth, wave_add, wave_diff

#Function to save waves as wav format audio file at 441.1 kHz sample rate
def wave_save(name, array):
	write(name+'.wav', 44100, array)

#Create a signal to later filter out

wave1 = sinusoid(10,1,20000)
sin1 = wave1.sine_wave()

wave2 = sinusoid(50,1,30000)
sin2 = wave2.sine_wave()

wave3 = sinusoid(100,1,15000)
sin3 = wave3.sine_wave()

#signal
add1 = wave_add(sin1,sin2,sin3)
#signal = wave_save('signal',add1)


add2 = wave_add(sin1,sin3)

#plt.plot(sin1)
#plt.plot(sin2)
#plt.plot(sin3)
plt.subplot(211)
plt.plot(add1)

plt.subplot(212)
plt.plot(add2)

plt.show()
