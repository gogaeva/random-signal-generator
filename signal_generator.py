import random
import math
import time

def generateSignal(harmonicNum, frequencyLimit, timeIntervalsNum):
    x = [0] * timeIntervalsNum
    omega0 = int(frequencyLimit / harmonicNum)
    for i in range(0, harmonicNum):
        omega = omega0 * (i + 1)
        A = random.random()
        phi = random.randint(0, omega-1)
        for t in range(0, timeIntervalsNum):
            xt = A * math.sin(omega * t + phi)
            x[t] += xt
    return x

def complexityTest(harmonicNum):
    intervals = [0] * harmonicNum
    for i in range(1, harmonicNum):
        start = time.time()
        _ = generateSignal(i, 2700, 256)
        intervals[i] = time.time() - start
    return intervals


