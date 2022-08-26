def generate_permutations(digit_range: int, length: int = -1, prefix=None):
    """
    The function uses recurrent algorithm to print all possible combinations of a given range of digits
    (range of digits must be >= length)
    :param digit_range: Given range of digits
    :param length: length of combinations
    :param prefix: prefix of combination, is used in generation to provide a recurrent case
    :returns: None
    :raise AssertionError if argument digit_range is less than length
    """
    assert digit_range >= length, AssertionError('Argument digit_range must be greater than or equal to length')
    prefix = prefix or []
    length = length if length != -1 else digit_range
    if length == 0:
        print(prefix)
        return
    for number in range(1, digit_range + 1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(digit_range, length - 1, prefix)
        prefix.pop()


generate_permutations(3, 3)
