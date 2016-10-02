import sys
import os
sys.path.append('../../software/models/')
from utilFunctions import wavread
import scipy.io.wavfile
import numpy as np

"""
A1-Part-1: Reading an audio file

Write a function that reads an audio file and returns 10 consecutive samples of the file starting from 
the 50001th sample. This means that the output should exactly contain the 50001th sample to the 50010th 
sample (10 samples). 

The input to the function is the file name (including the path) and the output should be a numpy array 
containing 10 samples.

If you use the wavread function from the utilFunctions module the input samples will be automatically 
converted to floating point numbers with a range from -1 to 1, which is what we want. 

Remember that in python, the index of the first sample of an array is 0 and not 1.

If you run your code using piano.wav as the input, the function should return the following 10 samples:  
[-0.06213569, -0.04541154, -0.02734458, -0.0093997 ,  0.00769066,	0.02319407,  0.03503525, 
0.04309214, 0.04626606,  0.0441908]
"""

INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}



def readAudio(inputFile):
    """
    Input:
        inputFile: the path to the wav file      
    Output:
        The function should return a numpy array that contains 10 samples of the audio.
    """
        
    sampleRate, audioData = scipy.io.wavfile.read(inputFile)

    if (len(audioData.shape) !=1):                                   # raise error if more than one channel
        raise ValueError("Audio file should be mono")
        
    if (sampleRate !=44100):                                         # raise error if more than one channel
        raise ValueError("Sampling rate of input sound should be 44100")

    if (len(audioData) < 50010):
        raise ValueError("Input sound should atleast have 50010 samples in it")

    #scale down and convert audio into floating point numbber in range of -1 to 1
    audioData = np.float32(audioData)/norm_fact[audioData.dtype.name]

    return audioData[50000:50010]

