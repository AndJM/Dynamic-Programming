"""This module contains data loading and visualization functionality."""

# import urllib2
import matplotlib.pyplot as plt
from math import sqrt
from random import shuffle
from tools import *

# URLs for data files
# PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
# HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
# FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
# CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
# WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"


def read_protein(filename):
    """
    Read a protein sequence from file and return a string representing the
    protein.
    """
    # protein_file = urllib2.urlopen(filename)
    with open(filename) as protein_file:
        protein_seq = protein_file.read()
        protein_seq = protein_seq.rstrip()
    return protein_seq


def read_scoring_matrix(filename):
    """
    Read a scoring matrix from file and return a dictionary of dictionaries
    mapping characters in the alphabet over which the matrix was defined to
    scores.
    """
    # table = urllib2.urlopen(filename)
    scoring_dict = {}
    with open(filename) as table:
        alphabet = table.readline()
        alphabet = alphabet.split()
        for line in table.readlines():
            scores = line.split()
            xkey = scores.pop(0)
            scoring_dict[xkey] = {}
            for ykey, score in zip(alphabet, scores):
                scoring_dict[xkey][ykey] = int(score)
    return scoring_dict


def human_fruitfly_alignment():
    """
    Return the local alignments of the sequences of HumanEyelessProtein and
    FruitflyEyelessProtein using the PAM50 scoring matrix.
    """
    scores = read_scoring_matrix('alg_PAM50.txt')
    human_protein = read_protein('alg_HumanEyelessProtein.txt')
    fly_protein = read_protein('alg_FruitflyEyelessProtein.txt')

    alignment_matrix = compute_alignment_matrix(human_protein,
                                                fly_protein,
                                                scores,
                                                'local')
    score, seq_human, seq_fly = compute_local_alignment(human_protein,
                                                        fly_protein,
                                                        scores,
                                                        alignment_matrix)
    print("The optimal alignment score:", score)
    print("The local alignment sequences of human and fruitfly proteins:\n")
    print(seq_human)
    print(seq_fly)


def consensus_alignment():
    """
    Compare the similarity of the two local alignment sequences (human and fly)
    to a third sequence, a "consensus" sequence of the PAX domain (the sequence
    of amino acids in the PAX domain in any organism).

    Return percentages of global alignment sequence elements that match (local
    human vs. consensus PAX and local fruitfly vs. consensus PAX).
    """
    scores = read_scoring_matrix('alg_PAM50.txt')
    human_protein = read_protein('alg_HumanEyelessProtein.txt')
    fly_protein = read_protein('alg_FruitflyEyelessProtein.txt')
    consensus_seq = read_protein('alg_ConsensusPAXDomain.txt')

    alignment_matrix = compute_alignment_matrix(human_protein,
                                                fly_protein,
                                                scores,
                                                'local')
    score, seq_human, seq_fly = compute_local_alignment(human_protein,
                                                        fly_protein,
                                                        scores,
                                                        alignment_matrix)
    alignment_matrix2 = compute_alignment_matrix(seq_human.replace('-', ''),
                                                 consensus_seq,
                                                 scores,
                                                 'global')
    local_human_consensus = compute_global_alignment(seq_human.replace('-', ''),
                                                     consensus_seq,
                                                     scores,
                                                     alignment_matrix2)
    alignment_matrix3 = compute_alignment_matrix(seq_fly.replace('-', ''),
                                                 consensus_seq,
                                                 scores,
                                                 'global')
    local_fly_consensus = compute_global_alignment(seq_fly.replace('-', ''),
                                                   consensus_seq,
                                                   scores,
                                                   alignment_matrix3)

    print("Percentage of global alignment sequence elements that match:\n"
          "local human vs. consensus PAX")
    print(string_compare(local_human_consensus[1], local_human_consensus[2]))
    print("local fruitfly vs. consensus PAX")
    print(string_compare(local_fly_consensus[1], local_fly_consensus[2]))


def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    """
    Input: two sequences 'seq_x' and 'seq_y', a 'scoring_matrix', and a number
    of trials 'num_trials'.

    Returns a dictionary 'scoring_distribution' that represents an
    un-normalized distribution via monte carlo simulation.
    """
    scoring_distribution = {}
    rand_list = list(seq_y)

    for _ in range(num_trials):
        shuffle(rand_list)
        rand_y = ''.join(rand_list)
        alignment_matrix = compute_alignment_matrix(seq_x,
                                                    rand_y,
                                                    scoring_matrix,
                                                    'local')
        score, *rest = compute_local_alignment(seq_x,
                                               rand_y,
                                               scoring_matrix,
                                               alignment_matrix)
        scoring_distribution[score] = scoring_distribution.get(score, 0) + 1

    return scoring_distribution


def make_plot_and_stats():
    """Return a bar plot of the normalized version of score_distribution."""
    scores = read_scoring_matrix('alg_PAM50.txt')
    human_protein = read_protein('alg_HumanEyelessProtein.txt')
    fly_protein = read_protein('alg_FruitflyEyelessProtein.txt')

    score_dist = generate_null_distribution(human_protein,
                                            fly_protein,
                                            scores,
                                            1000)
    xvals, yvals = [], []
    n = sum(score_dist.values())

    for key, val in score_dist.items():
        xvals.append(key)
        yvals.append(val/n)

    plt.bar(xvals, yvals)
    plt.title("Score distribution for 1000 trials of fruit fly \n and human"
              " local alignments using PAM50")
    plt.xlabel('Scores (fruitfly sequence randomized)')
    plt.ylabel('Normalized frequency')
    plt.show()

    print('Computing basic statistical analysis of this distribution...')
    mu = sum([key*val for key, val in score_dist.items()])/n
    print('The mean is', mu)
    sigma = sqrt(sum((key-mu)**2 for key in score_dist.keys()
                                 for _ in range(score_dist[key]))/n)
    print('The standard deviation is', sigma)
    alignment_matrix = compute_alignment_matrix(human_protein,
                                                fly_protein,
                                                scores,
                                                'local')
    s, *rest = compute_local_alignment(human_protein,
                                       fly_protein,
                                       scores,
                                       alignment_matrix)
    z = (s-mu)/sigma
    print('The z-score for the local alignment', s, 'is', z)


if __name__ == '__main__':
    human_fruitfly_alignment()
    consensus_alignment()
    # make_plot_and_stats()
    exit()
