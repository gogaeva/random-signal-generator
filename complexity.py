import signal_generator
import dft
import time
import math

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

def comparativeBenchmark(maximum):
    count = int(math.log2(maximum))
    signals = [0] * count
    for i in range(count):
        intervalCount = 1 << (i+1)
        signals[i] = signal_generator.generate(10, 2700, intervalCount)
    def executor(algorithm):
        times = [0] * count
        for i in range(count):
            start = time.perf_counter()
            _ = algorithm(signals[i])
            end = time.perf_counter()
            times[i] = end - start
        return times
    return executor




