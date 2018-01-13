## Dynamic Programming

### 1 Computing alignments of sequences

+ Dynamic programming (bottom-up) solution to the problem of sequence alignment
+ Algorithms are differentiated between computing local and global alignments of two sequences
+ Implements backtracking
+ Data files contain the amino acid sequences that form eyeless proteins in the human and fruit fly genomes and a widely agreed upon scoring matrix
+ Basic statistical analysis on the results indicate that alignments cannot be due to chance
+ Underlying distribution is produced using monte carlo methods
+ Produces one histogram using matplotlib

### 2 Spelling correction
+ Computes the edit distance of two strings using global alignment for sequences using an appropriate scoring matrix
+ The edit distance (a measure of dissimilarity) is related to the similarity of two strings (optimal global alignment)
+ Algorithm efficiency is considered
+ Data is a file of 79000+ words from the official Scrabble words list

### 3 Longest increasing subsequence
+ A dynamic programming solution to the longest increasing subsequence problem
+ Returns the length of a longest increasing sequence in an array in O(n^2) time
+ A second implementation returns a longest increasing sequence
+ A third implementation returns the length of a longest increasing sequence using patience sorting; runs in O(nlogn) time
+ Produces line plots using matplotlib to visually compare running times

### 4 0-1 knapsack problem
+ Implements three dynamic programs to solve the knapsack problem: choose a subset of items subject to the knapsack capacity that yield the maximum value over all items
+ The first implementation returns a matrix built bottom-up (row by row)
+ Auxillary routine uses backtracking to return the best items
+ A second implementation improves upon the use of space to O(capacity) by rewriting a single 1 x W+1 array instead of building the full n+1 x W+1 matrix
+ A third implementation return a knapsack's maximum value recursing through subproblems top-down
+ Uses the functools.lru_cache decorator
+ Concludes that caching reduces time (since not all subproblems need to be considered), yet lru_cache is too slow when params are sufficiently large
+ Concludes that recursion is not ideal, since recursion depth limits are exceeded for interesting problem instances
+ Performs unittesting using the doctest module (doctest.testmod)
+ Builds a small command line tool to process data
+ Produces line plots using matplotlib to compare running times
+ Data is from Prof. Van Hentenryck's Discrete Optimization course

### 5 Miscellaneous dynamic programming exercises
+ Problem: Count the number of ways to express a given positive integer N as an
unordered partition using only a provided set of integers S
+ A frog wants to get from position 0 to a given target position It can hop any
one of n fixed distances {s_0, s_1, ..., s_(n-1)}. Count the number of
different ways in which the frog can hop to the target position. Two hop
sequences are different they differ in at least one position (i.e., the frog
visits a position which is not visited in the other sequence).

Note that the solution will also count the number of ordered partitions of a
positive integer using only those in S.
+ """Dynamic progamming solution to the change-making problem"""
    Return the minimum number of coins of denominations given in coin_types
    totaling target_val, otherwise claim no solution exists.

    Note: coin_types need not be sorted, may contain duplicates, and does not
    need to contain 1.

    Space complexity: O(len(coin_types)) by rewriting one list.
    Time complexity: O(target_val * len(coin_types)) which is pseudo-polynomial
    since target_val is not constant in the general problem (consider its
    length in bits).
