import matplotlib.pyplot as plt
import signal_generator
import characteristics

HARMONIC_NUM = 10
FREQUENCY_LIMIT = 2700
TIME_INTERVALS_NUM = 256
TEST_HARMONIC_NUM = 1000     #for complexity test

plt.style.use("dark_background")

fig1, (ax1, ax2) = plt.subplots(2, 1)

t = list(range(TIME_INTERVALS_NUM))
signal = signal_generator.generateSignal(HARMONIC_NUM, FREQUENCY_LIMIT, TIME_INTERVALS_NUM)

ax1.plot(t, signal, color="red")
ax1.set_title("Random Signal")
ax1.set_xlabel("t")
ax1.set_ylabel("x")
ax1.grid()

n = list(range(TEST_HARMONIC_NUM))
time = signal_generator.complexityTest(TEST_HARMONIC_NUM)

ax2.plot(n, time, color="green")
ax2.set_title("Algorithm complexity")
ax2.set_xlabel("n")
ax2.set_ylabel("time")

fig2, (ax3, ax4, ax5) = plt.subplots(3, 1)

x = signal_generator.generateSignal(HARMONIC_NUM, FREQUENCY_LIMIT, TIME_INTERVALS_NUM)
y = signal_generator.generateSignal(HARMONIC_NUM, FREQUENCY_LIMIT, TIME_INTERVALS_NUM)
tau = list(range(TIME_INTERVALS_NUM))
crossCorrelation = characteristics.correlation(x, y)
autoCorrelation = characteristics.correlation(x, x)

ax3.plot(t, x, color="red", label="X")
ax3.plot(t, y, color="green", label="Y")
ax3.set_title("Random Signals")
ax3.set_xlabel("t")
ax3.set_ylabel("x")
ax3.grid()
ax3.legend()

ax4.plot(tau, crossCorrelation, color="purple")
ax4.set_title("Cross-correlation X and Y")
ax4.set_xlabel("tau")
ax4.set_ylabel("Rxy")
ax4.grid()

ax5.plot(tau, autoCorrelation, color="purple")
ax5.set_title("Autocorrelation X and X")
ax5.set_xlabel("tau")
ax5.set_ylabel("Rxx")
ax5.grid()

print("mx = ", characteristics.matexpectation(x))
print("Dx = ", characteristics.dispersion(x))
print("my = ", characteristics.matexpectation(y))
print("Dy = ", characteristics.dispersion(y))

plt.tight_layout()
plt.show()







