"""Knuth Morris Pratt (KMP) is an algorithm, which is used to search if a pattern is presented in a sequence.
The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we take advantage of this
information to avoid matching the characters that we know will anyway match. The time complexity of KMP is O(n).
"""


def kmp(pattern, sequence):
    """
    The function consists of two logical parts.
    First - preprocessing the searched pattern to define prefix-function (the longest prefix suffix values) for its
    elements, then using the values of prefix function to search for pattern in sequence
    :param pattern: searched pattern
    :param sequence: given sequence
    :return: None
    """
    def _process_pattern(processed_pattern):
        """
        The function preprocesses given pattern to return a list of the longest prefix suffix values for that pattern
        :param processed_pattern: given pattern
        :return: list
        """
        p_func_list = [0] * len(processed_pattern)
        j = 0  # length of the previous longest prefix suffix
        i = 1
        while i < len(processed_pattern):
            if processed_pattern[j] == processed_pattern[i]:
                p_func_list[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    p_func_list[i] = 0
                    i += 1
                else:
                    j = p_func_list[j - 1]
        return p_func_list

    p_list = _process_pattern(pattern)
    flag = False

    pat_length = len(pattern)
    seq_length = len(sequence)

    seq_pointer = 0
    pat_pointer = 0

    while seq_pointer < seq_length:
        if pat_pointer < pat_length and  sequence[seq_pointer] == pattern[pat_pointer]:
            seq_pointer += 1
            pat_pointer += 1
            if pat_pointer == len(pattern):
                print(f'pattern found at index {seq_pointer - pat_length}')
                flag = True
        else:
            if pat_pointer > 0:
                pat_pointer = p_list[pat_pointer - 1]
            else:
                seq_pointer += 1

    if seq_pointer == seq_length and not flag:
        print('pattern not found')


def test_kmp(test_pattern, test_sequence):
    print(f'Testing kmp function for:\nTest pattern: {test_pattern}\nTest sequence: {test_sequence}\nResult:')
    kmp(test_pattern, test_sequence)
    print()


test_kmp(test_pattern='fury', test_sequence='furyousfury')
test_kmp(test_pattern='furr', test_sequence='furyousfury')
test_kmp(test_pattern='', test_sequence='furyousfury')
test_kmp(test_pattern='furyousfury', test_sequence='')
