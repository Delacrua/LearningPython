"""The Levenshtein distance is a text similarity measure that compares two words and returns a numeric value
representing the distance between them. The distance reflects the total number of single-character edits required to
transform one word into another.
"""


def levenshtein(first, second):
    """
    The function searches for Levenshtein distance between given two sequences and writes result in a matrix form
    :param first: first sequence
    :param second: second sequence
    :return: Levenshtein distance
    """
    distance = [[i + j if i * j == 0 else 0 for j in range(len(second) + 1)] for i in range(len(first) + 1)]
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i - 1] == second[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(distance[i - 1][j - 1], distance[i - 1][j], distance[i][j - 1])
    return distance[-1][-1]


t_f1 = 'pineapple'
t_f2 = 'fine apples'

print(levenshtein(t_f1, t_f2))
