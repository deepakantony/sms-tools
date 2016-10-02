import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)
x_fft = fft(x)
mag = abs(x_fft)
phase = np.angle(x_fft)
