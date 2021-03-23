import matplotlib.pyplot as plt
import numpy as np
import signal_generator
import dft
import fft
import complexity

HARMONIC_NUM = 10
FREQUENCY_LIMIT = 2700
TIME_INTERVALS_NUM = 256
COMPARISON_INTERVALS_NUM = 2 ** 10
COMPLEXITY_INTERVALS_NUM = 2 ** 15

plt.style.use("dark_background")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
f = np.linspace(0, FREQUENCY_LIMIT, TIME_INTERVALS_NUM)
signal = signal_generator.generate(HARMONIC_NUM, FREQUENCY_LIMIT, TIME_INTERVALS_NUM)
spectrumNumPy = abs(np.fft.fft(signal))
spectrumFFT = abs(fft.transform(signal))
ax1.plot(f, spectrumNumPy, color="blue")
ax1.set_title("numpy")
ax2.plot(f, spectrumFFT, color="blue")
ax2.set_title("my fft")
counts = [1 << i for i in range(1, int(np.log2(COMPLEXITY_INTERVALS_NUM))+1)]
time = complexity.comparativeBenchmark(COMPLEXITY_INTERVALS_NUM)(fft.transform)
ax3.plot(counts, time, color="green", marker=".")
ax3.set_title("Algorithm complexity")
ax3.set_xlabel("Number of discrete intervals in signal")
ax3.set_ylabel("Time")


fig2, ax4 = plt.subplots()
benchmark = complexity.comparativeBenchmark(COMPARISON_INTERVALS_NUM)
counts = [1 << i for i in range(1, int(np.log2(COMPARISON_INTERVALS_NUM))+1)]
dftSpeed = benchmark(dft.transform)
fftSpeed = benchmark(fft.transform)
numpySpeed = benchmark(np.fft.fft)
ax4.plot(counts, dftSpeed, color="red", label="my dft", marker=".")
ax4.plot(counts, fftSpeed, color="orange", label="my fft", marker=".")
ax4.plot(counts, numpySpeed, color="green", label="numpy", marker=".")
ax4.set_title("Speed comparison")
ax4.legend()

plt.tight_layout()
plt.show()