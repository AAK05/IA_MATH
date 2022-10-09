import json
import matplotlib.pyplot as plt
import sys
from scipy.fft import rfftfreq,fftfreq
import numpy as np

def readjson(fname):
    with open(fname,"r") as f:
        return json.load(f)

def processdft(dft):
    complexdft = []
    for i in dft:
        complexdft.append(i[0]+1j*i[1])
    #print(complexdft[0:3])
    result = np.abs(complexdft)
    print(result[0:10])
    return result

def display(dft):
    x = fftfreq(len(dft),1/44100).tolist()
    print(x[1]==x[-1])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("|f̂(k)|")
    plt.plot(x,processdft(dft))
    plt.xlim(0,250)
    plt.ylim(bottom=0)
    plt.minorticks_on()
    plt.grid(which="both")
    plt.show()

def main():
    display(readjson(sys.argv[1]))

if __name__ == "__main__":
    main()