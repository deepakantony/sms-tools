import numpy as np
import  matplotlib.pyplot as plt
import sys
from scipy.signal import get_window
sys.path.append('../../software/models')
import dftModel as DFT


fs = 44100
M = 101
f = 5000.0
x = np.cos(2*np.pi*f*np.arange(M)/float(fs))
w = get_window('blackmanharris', M)
N =  512
mX,pX = DFT.dftAnal(x,w,N)

#print M
#print len(x)
#print len(w)
#print len(mX)

plt.plot(np.arange(0,fs/2+1,fs/float(N)), mX - max(mX))
plt.show()

