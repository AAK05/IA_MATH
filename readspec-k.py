import json #Library to load audio files
import numpy as np #General purpose math library
import sys #Library to interact with the system

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

def readindex(dft,k):
    i= dft[k]
    m = i[0]+1j*i[1]
    return np.abs(m)

if __name__ == "__main__":
    print(readindex(readjson(sys.argv[1]),int(sys.argv[2])))