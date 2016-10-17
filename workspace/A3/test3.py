import numpy as np
from scipy.fftpack import fft,ifft
from scipy.io.wavfile import read

def wavread(file):
    (fs,data) = read(file)
    if data.dtype == np.int16:
        data = np.float32(data)/(1<<15)
    elif data.dtype == np.int32:
        data = np.float32(data)/(1<<31)
    return (fs,data)

M = 501
hM1 = int((M+1)/2)
hM2 = int(M/2)

(fs,data) = wavread('../../sounds/soprano-E4.wav')
x = data[5000:5000+M] * np.hamming(M)

N = 256
fftbuf = np.zeros(N)
fftbuf[:hM1] = x[hM2:]
fftbuf[N-hM2:] = x[:hM2]
X = fft(fftbuf)
mX = 20*np.log10(abs(X[:N/2]))
pX = np.unwrap(np.angle(X))

y = np.real(ifft(X))
newx = np.zeros(M)
newx[:hM2] = y[N-hM2:]
newx[hM2:] = y[:hM1]


