import sys
import matplotlib
import matplotlib.pyplot as plt
import math_lib
matplotlib.use('Agg')


def boxplot(L, out_file):
    D = []
    for l in L:
        A = l.rstrip().split()
        D.append(float(A[0]))
        D.append(float(A[1]))
    mean = math_lib.list_mean(D)
    stdev = math_lib.list_stdev(D)
    fig, ax = plt.subplots(figsize=(3, 10), dpi=300)
    ax.boxplot(D)
    ax.set_title('mean: '+str(mean)+' stdev: '+str(stdev))
    ax.set_ylabel('Value')
    plt.savefig(out_file, bbox_inches='tight')


def histogram(L, out_file):
    D = []
    for l in L:
        A = l.rstrip().split()
        D.append(float(A[0]))
        D.append(float(A[1]))
    width = 3
    height = 3
    mean = math_lib.list_mean(D)
    stdev = math_lib.list_stdev(D)
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(D)
    ax.set_title('mean: '+str(mean)+' stdev: '+str(stdev))
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    plt.savefig(out_file, bbox_inches='tight')


def combo(L, out_file):
    X = []
    Y = []
    D = []
    for l in L:
        A = l.rstrip().split()
        X.append(float(A[0]))
        Y.append(float(A[1]))
        D.append(float(A[0]))
        D.append(float(A[1]))
    width = 5
    height = 3
    mean = math_lib.list_mean(D)
    stdev = math_lib.list_stdev(D)
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 2, 1)
    ax.boxplot(D)
    ax.set_ylabel('Values')
    ax = fig.add_subplot(1, 2, 2)
    ax.hist(D)
    ax.set_title('mean: '+str(mean)+' stdev: '+str(stdev))
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Values')
    plt.savefig(out_file, bbox_inches='tight')


if __name__ == '__main__':
    main()
