"""
An implementation of algorithm that searches for longest common subsequence of two sequences
"""


def lcs(first, second):
    """
    The function searches for length of the longest common subsequence of given two sequences and writes result in
    a matrix form
    :param first: first sequence
    :param second: second sequence
    :return: length of the longest common subsequence
    """
    result_matrix = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i - 1] == second[j - 1]:
                result_matrix[i][j] = 1 + result_matrix[i - 1][j - 1]
            else:
                result_matrix[i][j] = max(result_matrix[i - 1][j], result_matrix[i][j - 1])
    return result_matrix[-1][-1]


test_first = 'asdasdf'
test_second = 'aseasdd'

print(lcs(test_first, test_second))
