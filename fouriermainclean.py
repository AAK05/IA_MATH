import librosa #Library to load audio files
import numpy as np #General purpose math library
import json #Library to write and read JSON files
import concurrent.futures #Library for multicore and multithread processing

def audiosignal(file,offset,duration): #Function to load audio signal from file
    audio,sample_rate = librosa.load(file,offset=offset,duration=duration,sr=None,mono=True)
    N = len(audio)
    time = np.linspace(0,N/sample_rate,N)
    return time,audio

def manualdft1k(audio,k): #Function to calculate DFT for 1 value of k
    result = 0
    for n in range(len(audio)):
        result += audio[n]*np.exp(-2*np.pi*1j*(k*n/len(audio)))
    return result

def manualdft(audio): #Function to gather DFT values for all values of k into a list
    audioenum = enumerate(audio)
    result = []
    for k in range(len(audio)):
        result.append(manualdft1k(audio,k))
    return result

def manualdft1kthreadingnumpy(audio,k): #NumPy optimized manualdft1k() function
    audioarray = np.array(audio)
    audiolen = len(audio)
    knarray = k * np.linspace(0,audiolen-1,audiolen)
    wnarray = np.exp(-2*np.pi*1j/audiolen)
    resultarray = np.power(wnarray,knarray)
    resultarray = audioarray * resultarray
    result = np.sum(resultarray)
    return (k,result)

def writejson(data,fname): #Function to write data to JSON files
    with open(fname,"w") as f:
        json.dump(data,f)

def realim(data): #Function to format data
    result = [[np.real(i),np.imag(i)] for i in data]
    return result

if __name__ == "__main__":
    for i in range(0,51): #Time duration control on source signal
        t,audio = audiosignal("Default_20221120-204024.wav",4,0.1*i)
        result = []
        executor = concurrent.futures.ProcessPoolExecutor() #Multiprocessing to speed up calculation
        futures = [executor.submit(manualdft1kthreadingnumpy,audio,n) for n in range(len(audio))]
        for f in concurrent.futures.as_completed(futures):
            result.append(f.result())
            if f.result()[0]%10000==0:
                print(f.result())
        result.sort(key = lambda s:s[0])
        result = [i[1] for i in result]
        writejson(realim(result),"C2res{}.json".format(str(i))) #Writing DFT output to file