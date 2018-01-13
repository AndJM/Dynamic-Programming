from tools import *

def unit_test1():
    diag_score = 10
    off_diag_score = 4
    dash_score = -6

    alphabet = set(['A', 'C', 'T', 'G'])
    seq_x = 'AA'
    seq_y = 'TAAT'

    alignment_type = 'local'

    scoring_matrix = build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, alignment_type)

    assert(alignment_matrix ==
           [[0, 0, 0, 0, 0],
            [0, 4, 10, 10, 4],
            [0, 4, 14, 20, 14]])

    assert(compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix) ==
           (20, 'AA', 'AA'))

    return 'unit test 1 passes'


def unit_test2():
    diag_score = 2
    off_diag_score = -1
    dash_score = -1

    seq_x = 'happypedestrianwalker'
    seq_y = 'sadpedesxtriandriver'

    alphabet = set(seq_x) | set(seq_y)

    alignment_type = 'local'

    scoring_matrix = build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, alignment_type)

    assert(alignment_matrix ==
           [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 3, 2, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 4, 3, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
            [0, 0, 0, 2, 1, 3, 6, 5, 4, 3, 2, 1, 0, 0, 0, 2, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 3, 5, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 0, 0, 2, 1],
            [0, 2, 1, 0, 0, 2, 4, 7, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 1],
            [0, 1, 1, 0, 0, 1, 3, 6, 9, 9, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [0, 0, 0, 0, 0, 0, 2, 5, 8, 8, 10, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4],
            [0, 0, 0, 0, 0, 0, 1, 4, 7, 7, 9, 12, 15, 14, 13, 12, 11, 10, 9, 8, 7],
            [0, 0, 2, 1, 0, 0, 0, 3, 6, 6, 8, 11, 14, 17, 16, 15, 14, 13, 12, 11, 10],
            [0, 0, 1, 1, 0, 0, 0, 2, 5, 5, 7, 10, 13, 16, 19, 18, 17, 16, 15, 14, 13],
            [0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 6, 9, 12, 15, 18, 18, 17, 16, 15, 14, 13],
            [0, 0, 2, 1, 0, 0, 0, 0, 3, 3, 5, 8, 11, 14, 17, 17, 17, 16, 15, 14, 13],
            [0, 0, 1, 1, 0, 0, 0, 0, 2, 2, 4, 7, 10, 13, 16, 16, 16, 16, 15, 14, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 6, 9, 12, 15, 15, 15, 15, 15, 14, 13],
            [0, 0, 0, 0, 0, 2, 1, 2, 1, 0, 2, 5, 8, 11, 14, 14, 14, 14, 14, 17, 16],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 4, 7, 10, 13, 13, 16, 15, 14, 16, 19]])

    assert(compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix) ==
           (19, 'pedes-trian', 'pedesxtrian'))

    return 'unit test 2 passes'


if __name__ == '__main__':
    print(unit_test1())
    print(unit_test2())
    exit()
