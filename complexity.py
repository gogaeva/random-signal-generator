import signal_generator
import dft
import time

def generatorComplexity(intervalsNum):
    intervals = [0] * int(intervalsNum/10)
    next = 0
    for i in range(10, intervalsNum+10, 10):
        start = time.time()
        _ = signal_generator.generate(10, 2700, i)
        intervals[next] = time.time() - start
        next += 1
    return intervals

def dftCompexity(signalIntervalsNum):
    intervals = [0] * int(signalIntervalsNum/10)
    next = 0
    for i in range(10, signalIntervalsNum+10, 10):
        signal = signal_generator.generate(10, 2700, i)
        start = time.time()
        _ = dft.transform(signal)
        intervals[next] = time.time() - start
        next += 1
    return intervals

