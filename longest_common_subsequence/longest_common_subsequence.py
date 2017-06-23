def longest_common_subsequence(seq1, seq2):
    """
    Returns the longest common subsequence
    :param seq1: First sequence
    :param seq2: Second sequence
    :return: The longest common subsequence of two input sequences
    """
    len1 = len(seq1)
    len2 = len(seq2)
    sequences = [[0 for x in range(len2 + 1)] for x in range(len1 + 1)]
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 or j == 0:
                sequences[i][j] = 0
            elif seq1[i - 1] == seq2[j - 1]:
                sequences[i][j] = sequences[i - 1][j - 1] + 1
            else:
                sequences[i][j] = max(sequences[i - 1][j], sequences[i][j - 1])
    prev_selected = sequences[len1][len2]
    lcs = [''] * (prev_selected + 1)
    lcs[prev_selected] = '\0'  # End of line char
    i = len1
    j = len2
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs[prev_selected - 1] = seq1[i - 1]
            i -= 1
            j -= 1
            prev_selected -= 1
        elif sequences[i - 1][j] > sequences[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs


def main():
    """
    Driver function for testing.
    """
    seq1 = 'iiitv/algos'
    seq2 = 'iiitv/Odyssy'
    print('longest common subsequence is',
          longest_common_subsequence(seq1, seq2))


if __name__ == '__main__':
    main()
