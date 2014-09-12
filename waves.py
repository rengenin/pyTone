import numpy as np
from scipy import signal
from scipy.io.wavfile import write

class sinusoid:
	def __init__(self,Hz,L,scale,note='note'):
		self.Hz = Hz # Frequency in Hertz
		self.L = L # Length of tone in seconds
		self.S_r = 44100. #Sample rate in Hertz
		self.T_s = 1./self.S_r #Time sample 
		self.note = note #Optional Note value for given frequency (string)
		self.s = 32767. #Scaling factor to make audible tone
		self.scale = scale #Boolean to turn scaling on or off
		self.name = 'sine_'+str(self.Hz)+'_'+str(self.L)

	def sine_wave(self):
		self.t = np.arange(0., self.L, self.T_s) #Time array
		self.y_t = np.sin(2.*np.pi*self.Hz*self.t)
		if self.scale == True:
			#Scaled up wave amplitude to audible level
			self.y_t = np.int16(self.y_t/np.max(np.abs(self.y_t))*self.s)
			return self.y_t
		#Wave no scaling
		self.H = self.y_t
		return self.y_t

class square_wave:
	def __init__(self,Hz,L,scale,note='note'):
		self.Hz = Hz # Frequency in Hertz
		self.L = L # Length of tone in seconds
		self.S_r = 44100. #Sample rate in Hertz
		self.T_s = 1./self.S_r #Time sample 
		self.note = note #Optional Note value for given frequency (string)
		self.s = 32767. #Scaling factor to make audible tone
		self.scale = scale #Boolean to turn scaling on or off
		self.name = 'square_'+str(self.Hz)+'_'+str(self.L)

	def square_wave(self):
		self.t = np.arange(0., self.L, self.T_s) #Time array
		self.y_t = signal.square(2.*np.pi*self.Hz*self.t)
		if self.scale == True:
			#Scaled up wave amplitude to audible level
			self.y_t = np.int16(self.y_t/np.max(np.abs(self.y_t))*self.s)
			return self.y_t
		#Wave no scaling
		self.H = self.y_t
		return self.y_t

class saw_tooth:
	def __init__(self,Hz,L,scale,note='note'):
		self.Hz = Hz # Frequency in Hertz
		self.L = L # Length of tone in seconds
		self.S_r = 44100. #Sample rate in Hertz
		self.T_s = 1./self.S_r #Time sample 
		self.note = note #Optional Note value for given frequency (string)
		self.s = 32767. #Scaling factor to make audible tone
		self.scale = scale #Boolean to turn scaling on or off
		self.name = 'saw_'+str(self.Hz)+'_'+str(self.L)

	def saw_wave(self):
		self.t = np.arange(0., self.L, self.T_s) #Time array
		self.y_t = signal.sawtooth(2.*np.pi*self.Hz*self.t)
		if self.scale == True:
			#Scaled up wave amplitude to audible level
			self.y_t = np.int16(self.y_t/np.max(np.abs(self.y_t))*self.s)
			return self.y_t
		#Wave no scaling
		self.H = self.y_t
		return self.y_t

class wave_math:
	def __init__(self,*waves):
		self.waves = waves

	def wave_add(self):
	#Sums input arrays seperated by commas in input
		self.composite = sum(self.waves)
		return self.composite

	def wave_diff(self):
	#Takes the difference of arrays seperated by commas in input
	#order subtraction given by order of input arrays
		self.lst = [] #Creates list out of inputs
		self.sub = [] #1 element length list which holds subtracted values
		for self.wavs in self.waves:
		#Fill out list of input arrays (each element is an array)
			self.lst.append(self.wavs)
		self.sub.insert(0,self.lst[0])
		#Set first value equal to first input
		for n in xrange(1, len(self.lst)):
			#Subtract subsequent arrays and replace first element in 
			#sub with difference of subtraction
			self.sub.insert(0, self.sub[0] - self.lst[n])
		return self.sub[0] #return difference result
