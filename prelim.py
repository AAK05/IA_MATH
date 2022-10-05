import librosa

#audio_path = "C:\\Users\\Adrien\\OneDrive\\Documents\\Python\\Projects\\IA_MATH\\2022-03-27 20-49-06.wav"
#samples,sample_rate = librosa.load(audio_path, sr=None, mono=True,offset=2.2,duration=0.1)
audio_path = "C:\\Users\\Adrien\\OneDrive\\Documents\\Python\\Projects\\IA_MATH\\2022-03-28 16-09-04.wav"
samples,sample_rate = librosa.load(audio_path, sr=None, mono=True,offset=1.6,duration=0.5)
print(len(samples))
print(sample_rate)
duration = len(samples)/sample_rate
print(duration)

from librosa import display
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft,fftfreq
plt.figure()
librosa.display.waveshow(y=samples,sr=sample_rate)
plt.show()
n=len(samples)
T=1/sample_rate
yf=fft(samples)
xf=fftfreq(n,T)
fig,ax = plt.subplots()
ax.plot(xf,2.0/n * np.abs(yf[:n//2]))
#ax.plot(2.0/n * np.abs(yf[:n//2]))
plt.grid()
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()
