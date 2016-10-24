import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft
import math
import matplotlib.pyplot as plt

M = 63
w = get_window('blackmanharris',M)
hM1 = (M+1)/2
hM2 = M/2

N = 512
assert M <= N
hN = N/2
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = w[-hM1:]
fftbuffer[-hM2:] = w[:hM2]

X = fft(fftbuffer)
absx = abs(X)
absx[absx<np.finfo(float).eps] = np.finfo(float).eps
mX = 20*np.log10(absx)
pX = np.angle(X)

mX1 = np.zeros(N)
mX1[:hN] = mX[hN:]
mX1[hN:] = mX[:hN]
pX1 = np.zeros(N)
pX1[:hN] = pX[hN:]
pX1[hN:] = pX[:hN]

plt.plot(np.arange(-hN,hN)/float(N)*M, mX1-max(mX1))
plt.axis([-20,20,-100,0])
plt.show()

