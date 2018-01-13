"""
Dynamic programming solution to the longest increasing subsequence problem.
"""


def LIS(S):
    """
    Return the length of a longest increasing sequence in non-empty list s.
    Runs in O(n^2).

    >>> LIS([3, 12, 18, 5, 7, 17, 19, 20, 18, 21, 4, 5, 7])
    7
    >>> LIS([])
    0
    >>> LIS([3, 2, 6, 4, 5, 1])
    3
    >>> fast_LIS([3, -2, 6, -4, 5, -1])
    2
    >>> LIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    6
    >>> LIS([3])
    1
    >>> LIS([3, 3, 3, 3])
    1
    >>> LIS([5, 4, 3, 2, 1])
    1
    >>> LIS([7, 2, 8, 1, 3, 4, 10, 6, 9, 5])
    5
    >>> LIS([6, 3, 5, 10, 11, 2, 9, 14, 13, 7, 4, 8, 12])
    5
    """
    DP = [1] * len(S)
    for i in range(len(S)):
        for j in range(i):
            if S[i] > S[j]:
                DP[i] = max(DP[i], DP[j]+1)
    return max(DP) if DP else 0


def compute_longest_seq(S):
    """
    Return the first longest increasing sequence in non-empty list s.

    >>> compute_longest_seq([3, 12, 18, 5, 7, 17, 19, 20, 18, 21, 4, 5, 7])
    (7, [3, 5, 7, 17, 19, 20, 21])
    >>> compute_longest_seq([])
    (0, [])
    >>> compute_longest_seq([3, 2, 6, 4, 5, 1])
    (3, [3, 4, 5])
    >>> compute_longest_seq([3, -2, 6, -4, 5, -1])
    (2, [3, 6])
    >>> compute_longest_seq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    (6, [0, 4, 6, 9, 13, 15])
    >>> compute_longest_seq([3])
    (1, [3])
    >>> compute_longest_seq([3, 3, 3, 3])
    (1, [3])
    >>> compute_longest_seq([5, 4, 3, 2, 1])
    (1, [5])
    >>> compute_longest_seq([7, 2, 8, 1, 3, 4, 10, 6, 9, 5])
    (5, [2, 3, 4, 6, 9])
    >>> compute_longest_seq([6, 3, 5, 10, 11, 2, 9, 14, 13, 7, 4, 8, 12])
    (5, [3, 5, 10, 11, 14])
    """
    if not S:
        return (0, [])
    DP = [1] * len(S)
    pointers = [-1] * len(S)
    max_val, max_val_idx, seq = 1, 0, []
    for i in range(len(S)):
        for j in range(i):
            if S[i] > S[j] and DP[i] < DP[j] + 1:
                DP[i] = DP[j] + 1
                pointers[i] = j
        if DP[i] > max_val:
            max_val = DP[i]
            max_val_idx = i
    while max_val_idx != -1:
        seq.append(S[max_val_idx])
        max_val_idx = pointers[max_val_idx]
    return (max_val, seq[::-1])


def fast_LIS(S):
    """
    Return the length of a longest increasing sequence in non-empty list s
    using patience sorting. Runs in O(nlogn).

    >>> fast_LIS([3, 12, 18, 5, 7, 17, 19, 20, 18, 21, 4, 5, 7])
    7
    >>> fast_LIS([])
    0
    >>> fast_LIS([3, 2, 6, 4, 5, 1])
    3
    >>> fast_LIS([3, -2, 6, -4, 5, -1])
    2
    >>> fast_LIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    6
    >>> fast_LIS([3])
    1
    >>> fast_LIS([3, 3, 3, 3])
    1
    >>> fast_LIS([5, 4, 3, 2, 1])
    1
    >>> fast_LIS([7, 2, 8, 1, 3, 4, 10, 6, 9, 5])
    5
    >>> fast_LIS([6, 3, 5, 10, 11, 2, 9, 14, 13, 7, 4, 8, 12])
    5
    >>> fast_LIS([30, 10, 20, 50, 40, 80, 60])
    4
    >>> fast_LIS([13, 3, 3, 12])
    2
    >>> fast_LIS([3, 3, 3, 3, 4])
    2
    """
    piles = []
    for elem in S:
        lo, hi = 0, len(piles)-1
        while lo <= hi:
            m = (hi+lo)//2  # floor
            if piles[m] < elem:  # bisect_left
                lo = m + 1
            else:
                hi = m - 1
        if lo == len(piles):
            piles.append(elem)
        else:
            piles[lo] = elem
    return len(piles)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    exit()
