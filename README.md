### Computing alignments of sequences

+ Dynamic programming (bottom-up) solution to the problem of sequence alignment
+ See [tools.py](/sequence%20alignment/tools.py)
+ Algorithms are differentiated between computing local and global alignments of two sequences
+ Project implements backtracking
+ Data files contain the amino acid sequences that form eyeless proteins in the human and fruit fly genomes and a widely agreed upon scoring matrix
+ Basic statistical analysis on the results indicate that alignments cannot be due to chance
+ Underlying distribution is produced using monte carlo methods
+ Produces one histogram using matplotlib
+ See [load_and_print.py](/sequence%20alignment/load_and_print.py)

### Spelling correction

+ Project computes the edit distance of two strings using global alignment for sequences using an appropriate scoring matrix
+ See [tools.py](spelling%20correction/tools.py)
+ The edit distance (a measure of dissimilarity) is related to the similarity of two strings (optimal global alignment)
+ Algorithm efficiency is considered
+ See [load_and_print.py](spelling%20correction/load_and_print.py)
+ Data is a file of 79000+ words from the official Scrabble words list

### Longest increasing subsequence

+ A dynamic programming solution to the longest increasing subsequence problem
+ See [longest_subsequence.py](longest%20subsequence/longest_subsequence.py)
+ Returns the length of a longest increasing sequence in an array in O(n^2) time
+ A second implementation returns such a longest increasing sequence
+ A third implementation returns the length of a longest increasing sequence using patience sorting, running in O(nlogn) time
+ Produces line plots using matplotlib to visually compare running times
+ See [running_times.py](/longest%20subsequence/running_times.py)

### 0-1 knapsack problem

+ Implements three dynamic programs to solve the knapsack problem (generally stated as choosing a subset of items subject to the knapsack capacity that yields the maximum value over all items)
+ See [knapsack.py](/knapsack/knapsack.py)
+ The first implementation returns a matrix built bottom-up (row by row)
+ An auxillary routine uses backtracking to return the best items
+ A second implementation improves upon the use of space to O(capacity) by rewriting a single 1 x W+1 array instead of building the full (n+1) x (W+1) matrix
+ A third implementation return a knapsack's maximum value recursing through subproblems top-down
+ Uses the functools.lru_cache decorator
+ Concludes that caching reduces time (since not all subproblems need to be considered), yet lru_cache is too slow when params are sufficiently large
+ Concludes that recursion is not ideal, since recursion depth limits are exceeded for interesting problem instances
+ Performs unittesting using the doctest module (doctest.testmod)
+ Builds a small command line tool to process data
+ Produces line plots using matplotlib to compare running times
+ See [running_times.py](/knapsack/running_times.py)
+ Data is from Prof. Van Hentenryck's Discrete Optimization course
