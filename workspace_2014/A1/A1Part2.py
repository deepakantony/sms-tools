import sys
import os
sys.path.append('../../software/models/')
from utilFunctions import wavread

import scipy.io.wavfile
import numpy as np


"""
A1-Part-2: Basic operations with audio

Write a function that reads an audio file and returns the minimum and the maximum values of the audio 
samples in that file. 

The input to the function is the wav file name (including the path) and the output should be two floating 
point values.

If you run your code using oboe-A4.wav as the input, the function should return the following output:  
(-0.83486432, 0.56501967)
"""

INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}

def minMaxAudio(inputFile):
    """
    Input:
        inputFile: file name of the wav file (including path)
    Output:
        A tuple of the minimum and the maximum value of the audio samples, like: (min_val, max_val)
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

    return min(audioData), max(audioData)

    

    
