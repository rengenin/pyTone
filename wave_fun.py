#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from waves2 import sinusoid, square_wave, saw_tooth, wave_add, wave_diff

#Function to save waves as wav format audio file at 441.1 kHz sample rate
def wave_save(name, array):
	write(name+'.wav', 44100, array)

def main():
	try:
		#Create 2 second long, 2 Hz sine wave 
		wave1 = sinusoid(2.,2.,True)
		sin = wave1.sine_wave()

		#Create 2 second long, 2 Hz square wave
		wave2 = square_wave(2.,2.,True)
		square = wave2.square_wave()

		#Create 2 second long, 2 Hz saw wave
		wave3 = saw_tooth(2.,2.,True)
		saw = wave3.saw_wave()

		#Add waves together
		add = wave_add(sin,saw,square)
		#Subtract waves
		sub = wave_diff(sin,saw,square)

		plt.plot(sin)
		plt.plot(square)
		plt.plot(saw)
		plt.plot(add)
		plt.plot(sub)
		plt.show()

	except:
		print 'Program terminated'
		return

if __name__ == '__main__': 
    main()
