from scipy.fft import rfft,rfftfreq
import librosa
import numpy as np
import matplotlib.pyplot as plt
import json
import concurrent.futures
import time

def audiosignal(file,offset,duration):
    audio,sample_rate = librosa.load(file,offset=offset,duration=duration,sr=None,mono=True)
    N = len(audio)
    time = np.linspace(0,N/sample_rate,N)
    """if __name__=="__main__":
        plt.xlabel("time (s)")
        plt.ylabel("Sound pressure")
        plt.plot(time,audio)
        plt.show()"""
    return time,audio

def fouriertrans(file,offset,duration):
    audio,sample_rate = librosa.load(file,offset=offset,duration=duration,sr=None,mono=True)
    N = len(audio)
    print(audio[0:10])
    fourierspace = rfft(audio)
    freqs = rfftfreq(N,1/sample_rate)
    fouriermod = np.abs(fourierspace)
    """plt.plot(freqs,fouriermod)
    if __name__=="__main__":
        plt.show()"""
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

def testmatrix(audio):
    fhat = 0
    """for i in range(len(audio)):
        fhatel = (np.exp(-2*np.pi*1j/(len(audio))))**(i*k)
        fhatel *= audio[k]
        fhat += fhatel
    #fhat = fhat*audio[k]"""
    dftmatrix = []
    for n in range(len(audio)):
        flayer = []
        for i in range(len(audio)):
            fhatel = (np.exp(-2*np.pi*1j/(len(audio))))**(i*n)
            flayer.append(fhatel)
        dftmatrix.append(flayer)
    dftmatrix = np.asarray(dftmatrix)
    fhats = np.dot(dftmatrix,audio)
    return fhats

def manualdft1k(audio,k):
    result = 0
    for n in range(len(audio)):
        result += audio[n]*np.exp(-2*np.pi*1j*(k*n/len(audio)))
    return result

def manualdft(audio):
    audioenum = enumerate(audio)
    result = []
    for k in range(len(audio)):
        result.append(manualdft1k(audio,k))
    return result

def manualdft1kthreading(audio,k):
    result = 0
    for n in range(len(audio)):
        result += audio[n]*np.exp(-2*np.pi*1j*(k*n/len(audio)))
    return (k,result)

def manualdft1kthreadingnumpy(audio,k):
    audioarray = np.array(audio)
    audiolen = len(audio)
    knarray = k * np.linspace(0,audiolen-1,audiolen)
    wnarray = np.exp(-2*np.pi*1j/audiolen)
    resultarray = np.power(wnarray,knarray)
    resultarray = audioarray * resultarray
    result = np.sum(resultarray)
    return (k,result)

def writejson(data,fname):
    with open(fname,"w") as f:
        json.dump(data,f)

def realim(data):
    result = [[np.real(i),np.imag(i)] for i in data]
    return result

"""t,audio = audiosignal("D7susC.wav",3.1,5)
freqs,fouriers=fouriertrans("D7susC.wav",3.1,5)"""
#print(testmatrix(audio)[0:9])
#print(manualdft1k(audio,2))
#print(manualdft(audio)[0:9])
"""print(fouriers[0:9])"""
#audiosignal("2022-03-27 20-49-06.wav",1.9,1)
#fouriertrans("2022-03-27 20-49-06.wav",1.9,1)
#samplevismachine(0.1)
"""t1 = time.time()
manualdft1kthreadingnumpy(audio,2)
t2 = time.time()
manualdft1kthreading(audio,2)
t3 = time.time()
print(t2-t1,t3-t2)"""

"""print(manualdft1kthreadingnumpy(audio,2))
print(manualdft1kthreading(audio,2))"""

"""if __name__ == "__main__":
    for i in range(11,20):
        t,audio = audiosignal("D7susC.wav",3.1,0.01*i)
        freqs,fouriers=fouriertrans("D7susC.wav",3.1,0.01*i)
        result = []
        executor = concurrent.futures.ProcessPoolExecutor()
        futures = [executor.submit(manualdft1kthreadingnumpy,audio,n) for n in range(len(audio))]
        for f in concurrent.futures.as_completed(futures):
            result.append(f.result())
            if f.result()[0]%10000==0:
                print(f.result())
        result.sort(key = lambda s:s[0])
        result = [i[1] for i in result]
        writejson(realim(result),"D7susC0{}.json".format(str(i)))"""

t,audio = audiosignal("Default_20221120-204024.wav",4,5)


if __name__ == "__main__":
    for i in range(570,580):
        t,audio = audiosignal("Default_20221120-204024.wav",4,0.001*i)
        freqs,fouriers=fouriertrans("Default_20221120-204024.wav",4,0.001*i)
        result = []
        executor = concurrent.futures.ProcessPoolExecutor()
        futures = [executor.submit(manualdft1kthreadingnumpy,audio,n) for n in range(len(audio))]
        for f in concurrent.futures.as_completed(futures):
            result.append(f.result())
            if f.result()[0]%10000==0:
                print(f.result())
        result.sort(key = lambda s:s[0])
        result = [i[1] for i in result]
        writejson(realim(result),"C2res0{}.json".format(str(i)))