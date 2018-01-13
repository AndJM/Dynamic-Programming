"""Some tools for measuring the edit distance of two strings"""

import string
from timeit import default_timer
from tools import *


def edit_distance(seq_x, seq_y):
    """
    The dissimilarity of two strings (the minimum number of single character
    insertions, deletions, and substiutions to transform one string into
    another) is calculated using the similarity of the two strings.

    The values below are such that the score from the resulting global
    alignment yields the edit distance.
    """
    diag_score = 2
    off_diag_score = 1
    dash_score = 0
    a = set(seq_x) | set(seq_y)
    sm = build_scoring_matrix(a, diag_score, off_diag_score, dash_score)
    am = compute_alignment_matrix(seq_x, seq_y, sm, 'global')
    s, *rest = compute_global_alignment(seq_x, seq_y, sm, am)
    return len(seq_x) + len(seq_y) - s


def read_words(filename):
    """Load word list from the file and return list of strings."""
    # word_file = urllib2.urlopen(filename)
    with open(filename) as word_file:
        words = word_file.read()
        word_list = words.split('\n')
        word_list = word_list[:-1]
    print("Loaded", len(word_list), "words.")
    return word_list


def check_spelling(checked_word, dist, word_list):
    """
    Iterate through 'word_list' and returns the set of words that are within
    an edit distance 'dist' of the string 'checked_word'.
    """
    result = set([])
    for word in word_list:
        if edit_distance(checked_word, word) <= dist:
            result.add(word)
    return result


def example1():
    words = read_words('assets_scrabble_words3.txt')
    print(check_spelling("humble", 1, words))
    print(check_spelling("firefly", 2, words))


def quick_check(checked_word, word_list, dist=1):
    """
    Return words of edit distance 1 or 2 from checked_word in word_list.

    Adapted from P. Norvig 'How to Write a Spelling Corrector' 2007
    http://norvig.com/spell-correct.html
    """
    word_set = set(word_list)

    def edit_one(word):
        alphabet = string.ascii_lowercase
        splits = [(word[:k], word[k:]) for k in range(len(word)+1)]
        deletions = [L + R[1:] for L, R in splits]
        insertions = [L + a + R for L, R in splits for a in alphabet]
        substitutions = [L + a + R[1:] for L, R in splits for a in alphabet]
        return set(deletions + insertions + substitutions)

    def edit_two(word):
        return set([word2 for word1 in edit_one(word) for word2 in edit_one(word1)])

    if dist == 1:
        return [word for word in edit_one(checked_word) if word in word_list]
    elif dist == 2:
        return [word for word in edit_two(checked_word) if word in word_list]


def example2():
    words = read_words('assets_scrabble_words3.txt')
    print(quick_check("humble", words))
    print(quick_check("firefly", words))


if __name__ == '__main__':
    # example1()
    example2()
    exit()
