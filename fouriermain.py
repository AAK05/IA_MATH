from scipy.fft import rfft,rfftfreq
import librosa
import numpy as np
import matplotlib.pyplot as plt
import sys

def audiosignal(file,offset,duration):
    audio,sample_rate = librosa.load(file,offset=offset,duration=duration,sr=None,mono=True)
    N = len(audio)
    time = np.linspace(0,N/sample_rate,N)
    if __name__=="__main__":
        plt.xlabel("time (s)")
        plt.ylabel("Sound pressure")
        plt.plot(time,audio)
        plt.show()
    return time,audio

def fouriertrans(file,offset,duration):
    audio,sample_rate = librosa.load(file,offset=offset,duration=duration,sr=None,mono=True)
    N = len(audio)
    print(audio[0:10])
    fourierspace = rfft(audio)
    freqs = rfftfreq(N,1/sample_rate)
    fouriermod = np.abs(fourierspace)
    plt.plot(freqs,fouriermod)
    if __name__=="__main__":
        plt.show()
    print(sample_rate,N)
    return freqs,fourierspace

def samplevismachine(freq=1):
    #x = np.linspace(0,10*17/6,1000000)
    x = np.linspace(0,np.pi,1000000)
    y = [np.cos(6*np.pi*i) for i in x]
    plt.plot(x,y)
    plt.show()
    #yhat = [i*np.exp(-2*1j*np.pi*freq) for i in y]
    yhat = []
    index = 0
    for i in y:
       yhatel = i*np.exp(-2*1j*np.pi*freq*(index/(len(y))))
       yhat.append(yhatel)
       index += 1
    yhatsum = sum(yhat)
    print(yhatsum)
    yhatr = [np.real(i) for i in yhat]
    yhatim = [np.imag(i) for i in yhat]
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    plt.plot(yhatr,yhatim,linewidth=0.3)
    plt.grid()
    plt.show()

    xf = rfftfreq(len(x),len(x)*(6/17))
    yf = rfft(y)
    plt.plot(xf,np.abs(yf))
    plt.show()

audiosignal("D7susC.wav",3.1,5)
fouriertrans("D7susC.wav",3,1)
#audiosignal("2022-03-27 20-49-06.wav",1.9,1)
#fouriertrans("2022-03-27 20-49-06.wav",1.9,1)
samplevismachine(0.1)