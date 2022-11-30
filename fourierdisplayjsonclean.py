import json #Library to load audio files
import matplotlib.pyplot as plt #Library to generate graphs
import sys #Library to interact with the system
from scipy.fft import fftfreq #Library to help with DFT x-axis
import numpy as np #General purpose math library

def readjson(fname): #Function to read JSON data from file
    with open(fname,"r") as f:
        return json.load(f)

def processdft(dft): #Function to process DFT data
    complexdft = []
    for i in dft:
        complexdft.append(i[0]+1j*i[1])
    result = np.abs(complexdft)
    print(result[0:10])
    return result

def display(dft): #Function to display DFT data to graph
    x = fftfreq(len(dft),1/44100).tolist()
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("|f̂(k)|")
    plt.plot(x,processdft(dft))
    plt.xlim(0,100)
    plt.ylim(bottom=0,top=500)
    plt.minorticks_on()
    plt.grid(which="both")
    plt.show()

def main(): #main function, reads STDIN from terminal
    display(readjson(sys.argv[1]))

if __name__ == "__main__":
    main()