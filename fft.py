import numpy as np

def transform(signal):
    N = len(signal)
    if N == 1:
        return signal
    spectrum = np.zeros(N, complex)
    evens = transform(signal[::2])
    odds = transform(signal[1::2])
    l = int(N/2)
    for k in range(l):
        W = np.exp((2j * np.pi * k) / N)
        spectrum[k] = evens[k] + odds[k] * W
        spectrum[k+l] = evens[k] - odds[k] * W
    return spectrum
