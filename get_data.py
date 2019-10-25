import sys


def read_stdin_col(col_num):
    A = []
    L = []
    for line in sys.stdin:
        A = line.rstrip().split(' ')
        L.append(A[col_num])
    return L


if __name__ == '__main__':
    None
