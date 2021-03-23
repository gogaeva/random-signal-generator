import numpy as np

def transform(signal):
    N = len(signal)
    spectrum = np.zeros(N, complex)
    for n in range(N):
        for k in range(N):
            spectrum[n] += signal[k] * np.exp((2 * 1j * np.pi * k * n) / N)
    return spectrum







