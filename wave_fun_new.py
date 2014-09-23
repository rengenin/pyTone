#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from waves import sinusoid, square_wave, saw_tooth, wave_add, wave_diff

#Function to save waves as wav format audio file at 441.1 kHz sample rate
def wave_save(name, array):
	write(name+'.wav', 44100, array)

#def main():
#	try:
#Create 2 second long, 2 Hz sine wave 
wave1 = sinusoid(160.,5.,30000.)
sin1 = wave1.sine_wave()

wave2 = sinusoid(480.,5.,90000.)
sin2 = wave2.sine_wave()

wave3 = sinusoid(350.,5.,60000.)
sin3 = wave3.sine_wave()

#wave4 = sinusoid(900.,5.,180000)
#sin4 = wave4.sine_wave()

add = wave_add(sin1,sin2,sin3)
#sin = wave_save('500', sin1)
write('160+480+350+900-hz.wav',44100,add)


''' #Create 2 second long, 2 Hz square wave
wave2 = square_wave(2.,2.,True)
square = wave2.square_wave() '''


''' #Create 2 second long, 2 Hz saw wave
wave3 = saw_tooth(2.,2.,True)
saw = wave3.saw_wave() '''

#Add waves together
add = wave_add(sin1,sin2)
#Subtract waves
#sub = wave_diff(sin1,sin2)

#plt.plot(sin1)
#plt.plot(sin2)
#plt.plot(saw)
plt.plot(add)
plt.xlim(0,1000)
#plt.plot(sub)
plt.show()

#except:
#	print 'Program terminated'
#	return
#if __name__ == '__main__': 
#   main()
