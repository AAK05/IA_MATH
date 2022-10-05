from scipy.fft import rfft,rfftfreq
import librosa
import numpy as np
import matplotlib.pyplot as plt
import sys

def audiosignal(file,offset,duration):
    audio,sample_rate = librosa.load(file,offset=offset,duration=duration,sr=None,mono=True)
    N = len(audio)
    time = np.linspace(0,N/sample_rate,N)
    plt.plot(time,audio)
    if __name__=="__main__":
        plt.show()
    return time,audio

def fouriertrans(file,offset,duration):
    audio,sample_rate = librosa.load(file,offset=offset,duration=duration,sr=None,mono=True)
    N = len(audio)
    fourierspace = rfft(audio)
    freqs = rfftfreq(N,1/sample_rate)
    fouriermod = np.abs(fourierspace)
    plt.plot(freqs,fouriermod)
    if __name__=="__main__":
        plt.show()
    return freqs,fourierspace

audiosignal("2022-03-27 20-49-06.wav",1.9,1)
fouriertrans("2022-03-27 20-49-06.wav",1.9,1)