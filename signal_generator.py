import random
import math
import time

def generate(harmonicNum, frequencyLimit, timeIntervalsNum):
    x = [0] * timeIntervalsNum
    omega0 = int(frequencyLimit / harmonicNum)
    for i in range(0, harmonicNum):
        #start = time.perf_counter_ns()
        omega = omega0 * (i + 1)
        A = random.random()
        phi = random.randint(0, omega-1)
        for t in range(0, timeIntervalsNum):
            xt = A * math.sin(omega * t + phi)
            x[t] += xt
        #end = time.perf_counter_ns()
        #print(f"Harmonic #{i} generating time: {(end - start) / 1000} us")
    return x




