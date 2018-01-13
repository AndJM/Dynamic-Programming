import matplotlib.pyplot as plt
from timeit import default_timer
from random import randrange
from knapsack import *


def make_plot():
    """
    Running-time comparison of the algorithms.
    """
    seq_vals = randrange
    number_of_items = range(10, 1000, 10)
    times1 = []
    times2 = []
    # times3 = []

    import gc
    gc.disable()  # to remove the spikes in the plot

    for size in number_of_items:
        values = [seq_vals(0, 100) for _ in range(size)]
        weights = [seq_vals(0, 100) for _ in range(size)]
        # capacity = seq_vals(0, 200)  # random capacity
        capacity = size // 2  # capacity varying with size
        # capacity = 50  # constant capacity

        start_time = default_timer()
        build_table(values, weights, capacity)[-1][-1]
        t = default_timer() - start_time
        times1.append(t)

        start_time = default_timer()
        knapsack(values, weights, capacity)
        t = default_timer() - start_time
        times2.append(t)

        # start_time = default_timer()
        # recursive_knapsack(values, weights, capacity)
        # t = default_timer() - start_time
        # times3.append(t)

    gc.enable()

    plt.plot(number_of_items, times1, '-b', label='Stores the full d.p. table')
    plt.plot(number_of_items, times2, '-g', label='Rewrites a single array')
    # plt.plot(number_of_items, times3, '-r', label='Recursive implementation')
    plt.title('Comparison of knapsack implementation running times\n '
              'on desktop Python with random capacity')
    plt.xlabel('number of items')
    plt.ylabel('Time (sec)')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    make_plot()
    exit()
