import matplotlib.pyplot as plt
from timeit import default_timer
from random import randrange
from longest_subsequence import *


def make_plot():
    """
    Running-time comparison of the algorithms.
    """
    seq_vals = randrange
    tests = range(100, 5001, 100)
    times1 = []
    times2 = []

    import gc
    gc.disable()  # to remove the spikes in the plot

    for seq_size in tests:
        seq = [seq_vals(0, 100) for _ in range(seq_size)]

        start_time = default_timer()
        LIS(seq)
        t = default_timer() - start_time
        times1.append(t)

        start_time = default_timer()
        fast_LIS(seq)
        t = default_timer() - start_time
        times2.append(t)

    gc.enable()

    plt.plot(tests, times1, '-r', label='$O(n^2)$ ')
    plt.plot(tests, times2, '-b', label='$O(n\log(n))$')
    plt.title('Comparison of longest increasing sequence \n'
              'implementations running times on desktop Python')
    plt.xlabel('sequence size')
    plt.ylabel('Time (sec)')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    make_plot()
    exit()
