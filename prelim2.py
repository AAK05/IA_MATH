from matplotlib import pyplot as plt
#from scipy.fft import fft,fftfreq
from scipy.fft import rfft,rfftfreq
import librosa
import numpy as np

#Loading in the audio
#audio_path = "C:\\Users\\Adrien\\OneDrive\\Documents\\Python\\Projects\\IA_MATH\\2022-03-28 16-09-04.wav"
#audio,sample_rate = librosa.load(audio_path, sr=None, mono=True,offset=1.6,duration=0.5) #For 2022-03-28 file
audio_path = "C:\\Users\\Adrien\\OneDrive\\Documents\\Python\\Projects\\IA_MATH\\2022-03-27 20-49-06.wav"
audio_path_mac = "/Users/Adrien/Library/CloudStorage/OneDrive-Personal/Documents/Python/Projects/IA_MATH/2022-03-27 20-49-06.wav"
try:
    audio,sample_rate = librosa.load(audio_path, sr=None, mono=True,offset=1.9,duration=1) #For 2022-03-27 file
except:
    audio,sample_rate = librosa.load(audio_path_mac, sr=None, mono=True,offset=1.9,duration=1)
#audio_path = "C:\\Users\\Adrien\\OneDrive\\Documents\\Python\\Projects\\IA_MATH\\New Recording 6.m4a"
#audio,sample_rate = librosa.load(audio_path, sr=None, mono=True,offset=1.4,duration=1.0) #For New Recording 6.m4a
N = len(audio)

#Displaying the audio waveform
time = np.linspace(0,N/sample_rate,num=N)
plt.plot(time,audio)
plt.show()

#Displaying the Fourier Transform
#Note: fft() outputs positive and negative, rfft() only outputs positive to save calculation time
yf = rfft(audio)
xf = rfftfreq(N,1/sample_rate)
plt.plot(xf,np.abs(yf))
plt.show()