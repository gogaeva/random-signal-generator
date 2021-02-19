def matexpectation(signal):
    return sum(signal) / len(signal)

def dispersion(signal):
    n = len(signal)
    mx = matexpectation(signal)
    deviations = [0] * n
    for i in range(n):
        xi = signal[i]
        deviations[i] = (xi - mx) ** 2
    return sum(deviations) / (n - 1)

def correlation(signalX, signalY):
    n = len(signalX)
    mx = matexpectation(signalX)
    my = matexpectation(signalY)
    R = [0] * n
    for tau in range(n - 1):
        for t in range(n - tau):
            R[tau] += (signalX[t] - mx) * (signalY[t + tau] - my)
        R[tau] /= (n - tau)
    return R
