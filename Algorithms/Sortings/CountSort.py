"""This sorting algorithm has time complexity of O(n+m) and is especially effective in some corner cases
(like small range of collection elements variants) and in such cases has algorithmic complexity close to O(n)
"""


def count_sort(unsorted_list: list):
    """
    The function sorts a list of integers using frequency analysis
    """
    freq_dict = {}
    result = []
    for i in unsorted_list:
        freq_dict[i] = freq_dict.get(i, 0) + 1
    for i in sorted(freq_dict):
        result.extend([i] * freq_dict[i])
    return result


test_list = [1, 3, 2, 4, 5, 0, 4, 7, 9, 2, 5, 4, 3, 5, 7, 8, 3, 2, 5, 4, 0, 2, 3, 4, 6, 7]

print(count_sort(test_list))
