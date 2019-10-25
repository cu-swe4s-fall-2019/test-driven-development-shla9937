import math


def list_mean(L):
    total = 0
    for num in L:
        total += num
    mean = total/len(L)
    return float(mean)


def list_stdev(L):
    n = len(L)
    if n <= 1:
        return None

    mean, sd = list_mean(L), 0.0
    for el in L:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))
    return sd
