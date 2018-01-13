"""A bottom-up implementation of the dynamic programming algorithm solving the 0-1 knapsack problem"""


def build_table(values, weights, capacity):
    """
    (list, list, int) -> list of lists (2-d array)

    Return the n+1 by W+1 (item number, capacity) matrix resulting from running
    dynamic programming, bottom-up (row by row), by choosing a subset of items
    subject to the knapsack capacity.

    Note that the indexing for the matrix and the items is offset by 1.
    """
    DP = [[0] * (capacity+1) for _ in range(len(values)+1)]
    for i in range(1, len(values)+1):
        for w in range(1, capacity+1):
            if weights[i-1] > w:
                DP[i][w] = DP[i-1][w]
            else:
                DP[i][w] = max(DP[i-1][w], values[i-1] + DP[i-1][w - weights[i-1]])
    return DP


def solve(dp_table):
    """
    Return the maximum value located at position DP[len(items)][capacity]. Used
    for unittesting.

    >>> solve(build_table([5, 6, 3], [4, 5, 2], 4))
    5
    >>> solve(build_table([5, 6, 3], [4, 5, 2], 5))
    6
    >>> solve(build_table([5, 6, 3], [4, 5, 2], 8))
    9
    >>> solve(build_table([5, 6, 3], [4, 5, 2], 10))
    11
    >>> solve(build_table([5, 6, 3], [4, 5, 2], 11))
    14
    >>> solve(build_table([1, 4, 5, 7], [1, 3, 4, 5], 7))
    9
    >>> solve(build_table([10, 4, 7], [4, 2, 3], 5))
    11
    >>> solve(build_table([4, 2, 6, 1, 2], [12, 1, 4, 1, 2], 15))
    11
    >>> solve(build_table([4, 6, 2, 1, 2], [12, 4, 1, 1, 2], 15))
    11
    >>> solve(build_table([1, 2, 4, 2, 6], [1, 2, 12, 1, 4], 15))
    11
    >>> solve(build_table([10, 40, 30, 50], [5, 4, 6, 3], 10))
    90
    >>> solve(build_table([150, 35, 200, 160, 60, 45, 60, 40, 30, 10, 70, 30, 15, 10, 40, 70, 75, 80, 20, 12, 50, 10], [9, 13, 153, 50, 15, 68, 27, 39, 23, 52, 11, 32, 24, 48, 73, 42, 43, 22, 7, 18, 4, 30], 400))
    1030
    >>> solve(build_table([3, 1, 3, 4, 3, 6], [3, 4, 8, 10, 15, 20], 32))
    12
    """
    return dp_table[-1][-1]


def backtrack(values, weights, capacity, dp_table):
    """
    Return both the items that maximize the value of the knapsack in sorted
    order and the maximum value.

    >>> args = [[5, 6, 3], [4, 5, 2], 4]; backtrack(*args, build_table(*args))
    (5, [(5, 4)])
    >>> args = [[5, 6, 3], [4, 5, 2], 5]; backtrack(*args, build_table(*args))
    (6, [(6, 5)])
    >>> args = [[5, 6, 3], [4, 5, 2], 8]; backtrack(*args, build_table(*args))
    (9, [(6, 5), (3, 2)])
    >>> args = [[5, 6, 3], [4, 5, 2], 10]; backtrack(*args, build_table(*args))
    (11, [(5, 4), (6, 5)])
    >>> args = [[5, 6, 3], [4, 5, 2], 11]; backtrack(*args, build_table(*args))
    (14, [(5, 4), (6, 5), (3, 2)])
    >>> args = [[1, 4, 5, 7], [1, 3, 4, 5], 7]; backtrack(*args, build_table(*args))
    (9, [(4, 3), (5, 4)])
    >>> args = [[10, 4, 7], [4, 2, 3], 5]; backtrack(*args, build_table(*args))
    (11, [(4, 2), (7, 3)])
    >>> args = [[4, 2, 6, 1, 2], [12, 1, 4, 1, 2], 15]; backtrack(*args, build_table(*args))
    (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    >>> args = [[4, 6, 2, 1, 2], [12, 4, 1, 1, 2], 15]; backtrack(*args, build_table(*args))
    (11, [(6, 4), (2, 1), (1, 1), (2, 2)])
    >>> args = [[1, 2, 4, 2, 6], [1, 2, 12, 1, 4], 15]; backtrack(*args, build_table(*args))
    (11, [(1, 1), (2, 2), (2, 1), (6, 4)])
    >>> args = [[10, 40, 30, 50], [5, 4, 6, 3], 10]; backtrack(*args, build_table(*args))
    (90, [(40, 4), (50, 3)])
    >>> args = [[150, 35, 200, 160, 60, 45, 60, 40, 30, 10, 70, 30, 15, 10, 40, 70, 75, 80, 20, 12, 50, 10], [9, 13, 153, 50, 15, 68, 27, 39, 23, 52, 11, 32, 24, 48, 73, 42, 43, 22, 7, 18, 4, 30], 400]; backtrack(*args, build_table(*args))
    (1030, [(150, 9), (35, 13), (200, 153), (160, 50), (60, 15), (60, 27), (70, 11), (70, 42), (75, 43), (80, 22), (20, 7), (50, 4)])
    >>> args = [[3, 1, 3, 4, 3, 6], [3, 4, 8, 10, 15, 20], 32]; backtrack(*args, build_table(*args))
    (12, [(3, 3), (3, 8), (6, 20)])
    """
    items = []
    j = capacity
    for i in range(len(values), 0, -1):
        if dp_table[i][j] != dp_table[i-1][j]:
            items.append((values[i-1], weights[i-1]))
            j -= weights[i-1]
    return dp_table[-1][-1], items[::-1]


def knapsack(values, weights, capacity):
    """
    (list, list, int) -> int

    Return a knapsack's maximum value by rewriting a single list. An improvement
    in space to O(capacity).

    >>> knapsack([5, 6, 3], [4, 5, 2], 4)
    5
    >>> knapsack([5, 6, 3], [4, 5, 2], 5)
    6
    >>> knapsack([5, 6, 3], [4, 5, 2], 8)
    9
    >>> knapsack([5, 6, 3], [4, 5, 2], 10)
    11
    >>> knapsack([5, 6, 3], [4, 5, 2], 11)
    14
    >>> knapsack([1, 4, 5, 7], [1, 3, 4, 5], 7)
    9
    >>> knapsack([10, 4, 7], [4, 2, 3], 5)
    11
    >>> knapsack([4, 2, 6, 1, 2], [12, 1, 4, 1, 2], 15)
    11
    >>> knapsack([4, 6, 2, 1, 2], [12, 4, 1, 1, 2], 15)
    11
    >>> knapsack([1, 2, 4, 2, 6], [1, 2, 12, 1, 4], 15)
    11
    >>> knapsack([10, 40, 30, 50], [5, 4, 6, 3], 10)
    90
    >>> knapsack([150, 35, 200, 160, 60, 45, 60, 40, 30, 10, 70, 30, 15, 10, 40, 70, 75, 80, 20, 12, 50, 10], [9, 13, 153, 50, 15, 68, 27, 39, 23, 52, 11, 32, 24, 48, 73, 42, 43, 22, 7, 18, 4, 30], 400)
    1030
    >>> knapsack([3, 1, 3, 4, 3, 6], [3, 4, 8, 10, 15, 20], 32)
    12
    """
    DP = [0]*(capacity+1)
    n = len(values)  # number of items
    for i in range(n):
        for w in range(capacity, 0, -1):
            if weights[i] > w:
                break
            else:
                DP[w] = max(DP[w], values[i] + DP[w - weights[i]])
    return DP[-1]


def recursive_knapsack(values, weights, capacity):
    """
    (list, list, int) -> (int, list)

    Return a knapsack's maximum value recursing through subproblems top-down.

    >>> recursive_knapsack([5, 6, 3], [4, 5, 2], 4)
    (5, [(5, 4)])
    >>> recursive_knapsack([5, 6, 3], [4, 5, 2], 5)
    (6, [(6, 5)])
    >>> recursive_knapsack([5, 6, 3], [4, 5, 2], 8)
    (9, [(6, 5), (3, 2)])
    >>> recursive_knapsack([5, 6, 3], [4, 5, 2], 10)
    (11, [(5, 4), (6, 5)])
    >>> recursive_knapsack([5, 6, 3], [4, 5, 2], 11)
    (14, [(5, 4), (6, 5), (3, 2)])
    >>> recursive_knapsack([1, 4, 5, 7], [1, 3, 4, 5], 7)
    (9, [(4, 3), (5, 4)])
    >>> recursive_knapsack([10, 4, 7], [4, 2, 3], 5)
    (11, [(4, 2), (7, 3)])
    >>> recursive_knapsack([4, 2, 6, 1, 2], [12, 1, 4, 1, 2], 15)
    (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    >>> recursive_knapsack([4, 6, 2, 1, 2], [12, 4, 1, 1, 2], 15)
    (11, [(6, 4), (2, 1), (1, 1), (2, 2)])
    >>> recursive_knapsack([1, 2, 4, 2, 6], [1, 2, 12, 1, 4], 15)
    (11, [(1, 1), (2, 2), (2, 1), (6, 4)])
    >>> recursive_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 10)
    (90, [(40, 4), (50, 3)])
    >>> recursive_knapsack([3, 1, 3, 4, 3, 6], [3, 4, 8, 10, 15, 20], 32)
    (12, [(3, 3), (3, 8), (6, 20)])
    """
    from functools import lru_cache

    @lru_cache()
    def dp_table(i, j):
        if i == 0:
            return 0
        if weights[i-1] > j:
            return dp_table(i-1, j)
        else:
            return max(dp_table(i-1, j),
                       dp_table(i-1, j - weights[i-1]) + values[i-1])

    items = []
    j = capacity
    for i in range(len(values), 0, -1):
        if dp_table(i, j) != dp_table(i-1, j):
            items.append((values[i-1], weights[i-1]))
            j -= weights[i-1]
    # print(dp_table.cache_info())
    return dp_table(len(values), capacity), items[::-1]


def main(filename):
    with open(filename, 'r') as data_file:
        first_line = next(data_file).strip()
        size, capacity = map(int, first_line.split())
        print('Number of items: {0}'.format(size))
        print('Knapsack capacity: {0}'.format(capacity))

        remaining_lines = [map(int, line.split()) for line in data_file]
        values, weights = zip(*remaining_lines)

        # dp_table = build_table(values, weights, capacity)
        # maxvalue, items = backtrack(values, weights, capacity, dp_table)
        # print('Max value possible: {0}'.format(maxvalue))
        # print('Take items: {0}'.format(items))

        print('Computing maximum value...\n')
        maxvalue = knapsack(values, weights, capacity)
        print('Maximum knapsack value: {0}'.format(maxvalue))


if __name__ == '__main__':
    # import doctest
    # print(doctest.testmod())

    import sys
    if len(sys.argv) != 2:
        sys.stderr.write('usage: {0} [file]\n'.format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
