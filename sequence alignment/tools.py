"""Basic analytic tools for aligning sequences"""


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    (set, int, int, int) -> dict

    Input: a set of characters in 'alphabet' and three scores 'diag_score',
    'off_diag_score', and 'dash_score'.

    Return a dictionary of dictionaries with entries indexed by pairs of
    characters in 'alphabet' plus '-'.

    The score for any entry indexed by one or more dashes is 'dash_score'. The
    score for the remaining diagonal entries is 'diag_score'. The score for the
    remaining off-diagonal entries is 'off_diag_score'.
    """
    symbols = alphabet | {'-'}

    def score(row, col):
        """helper function"""
        if row == '-' or col == '-':
            return dash_score
        elif row == col:
            return diag_score
        return off_diag_score

    return {row: {col: score(row, col) for col in symbols} for row in symbols}


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, alignment='global'):
    """
    (str, str, dict, str) -> dict

    Input: two sequences 'seq_x' and 'seq_y' whose elements share a common
    alphabet with the scoring matrix 'scoring_matrix'.

    Return the alignment matrix for 'seq_x' and 'seq_y'.

    'alignment' can be set to 'global' or 'local' and specifies the method to
    compute the alignment matrix used to solve the Global or Local Pairwise
    Alignment Problem, respectively.
    """
    x_length, y_length = len(seq_x), len(seq_y)
    alignment_matrix = [[0 for col in range(y_length + 1)] for row in range(x_length + 1)]

    if alignment == 'global':
        for i in range(1, x_length+1):
            alignment_matrix[i][0] = alignment_matrix[i-1][0] + \
                                    scoring_matrix[seq_x[i-1]]['-']
        for j in range(1, y_length+1):
            alignment_matrix[0][j] = alignment_matrix[0][j-1] + \
                                    scoring_matrix['-'][seq_y[j-1]]
        for i in range(1, x_length+1):
            for j in range(1, y_length+1):
                x, y = seq_x[i-1], seq_y[j-1]
                s1 = alignment_matrix[i-1][j-1] + scoring_matrix[x][y]
                s2 = alignment_matrix[i][j-1] + scoring_matrix['-'][y]
                s3 = alignment_matrix[i-1][j] + scoring_matrix[x]['-']
                alignment_matrix[i][j] = max(s1, s2, s3)

    elif alignment == 'local':
        for i in range(1, x_length+1):
            alignment_matrix[i][0] = max(0, alignment_matrix[i-1][0] +
                                         scoring_matrix[seq_x[i-1]]['-'])
        for j in range(1, y_length+1):
            alignment_matrix[0][j] = max(0, alignment_matrix[0][j-1] +
                                         scoring_matrix['-'][seq_y[j-1]])
        for i in range(1, x_length+1):
            for j in range(1, y_length+1):
                x, y = seq_x[i-1], seq_y[j-1]
                s1 = alignment_matrix[i-1][j-1] + scoring_matrix[x][y]
                s2 = alignment_matrix[i][j-1] + scoring_matrix['-'][y]
                s3 = alignment_matrix[i-1][j] + scoring_matrix[x]['-']
                alignment_matrix[i][j] = max(0, s1, s2, s3)

    return alignment_matrix


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    (str, str, dict, list) -> tuple

    Input: two sequences 'seq_x' and 'seq_y' whose elements share a common
    alphabet with the scoring matrix 'scoring_matrix'.

    Return a global alignment of 'seq_x' and 'seq_y' using the global alignment
    matrix 'alignment_matrix'. Output is a tuple of the form
    (score, align_x, align_y) where score is the score of the global alignment
    'align_x' and 'align_y'.
    """
    align_x, align_y = '', ''
    i, j = len(seq_x), len(seq_y)

    while i > 0 and j > 0:
        if alignment_matrix[i][j] == alignment_matrix[i-1][j-1] + \
                                    scoring_matrix[seq_x[i-1]][seq_y[j-1]]:
            align_x = seq_x[i-1] + align_x
            align_y = seq_y[j-1] + align_y
            i -= 1
            j -= 1
        elif alignment_matrix[i][j] == alignment_matrix[i][j-1] + \
                                      scoring_matrix['-'][seq_y[j-1]]:
            align_x = '-' + align_x
            align_y = seq_y[j-1] + align_y
            j -= 1
        else:
            align_x = seq_x[i-1] + align_x
            align_y = '-' + align_y
            i -= 1

    while i > 0:
        align_x = seq_x[i-1] + align_x
        align_y = '-' + align_y
        i -= 1
    while j > 0:
        align_x = '-' + align_x
        align_y = seq_y[j-1] + align_y
        j -= 1

    return (alignment_matrix[len(seq_x)][len(seq_y)], align_x, align_y)


def max_entry(matrix):
        """
        list -> tuple

        Return (max element, index) in matrix specified as a list of lists.
        """
        m = float('-inf')
        idx, idy = 0, 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                elem = matrix[i][j]
                if elem > m:
                    m = elem
                    idx, idy = i, j
        return (m, idx, idy)


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    (str, str, dict, list) -> tuple

    Input: two sequences 'seq_x' and 'seq_y' whose elements share a common
    alphabet with the scoring matrix 'scoring_matrix'.

    Return a local alignment of 'seq_x' and 'seq_y' using the local alignment
    matrix 'alignment_matrix'. Output is a tuple of the form
    (score, align_x, align_y) where score is the score of the optimal local
    alignment 'align_x' and 'align_y'.
    """
    align_x, align_y = '', ''
    m, i, j = max_entry(alignment_matrix)

    while alignment_matrix[i][j] > 0:
        if alignment_matrix[i][j] == alignment_matrix[i-1][j-1] + \
                                    scoring_matrix[seq_x[i-1]][seq_y[j-1]]:
            align_x = seq_x[i-1] + align_x
            align_y = seq_y[j-1] + align_y
            i -= 1
            j -= 1
        elif alignment_matrix[i][j] == alignment_matrix[i][j-1] + \
                                      scoring_matrix['-'][seq_y[j-1]]:
            align_x = '-' + align_x
            align_y = seq_y[j-1] + align_y
            j -= 1
        else:
            align_x = seq_x[i-1] + align_x
            align_y = '-' + align_y
            i -= 1

    return (m, align_x, align_y)


def string_compare(x, y):
    """
    (str, str) -> float

    Return the ratio of matching characters in strings x, y to the length of
    the larger string.
    """
    k = 0
    for i in range(min(len(x), len(y))):
        if x[i] == y[i]:
            k += 1
    return k / max(len(x), len(y))
