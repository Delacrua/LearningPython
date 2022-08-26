def generate_numbers(base: int, length: int, prefix=None):
    """
    The function uses recurrent algorithm to print all possible numbers of given length in given counting system base
    (with insignificant zeroes)
    :param base: Counting system base
    :param length: max length of numbers in digits
    :param prefix: prefix of number, is used in generation to provide a recurrent case
    :returns: None
    """
    prefix = prefix or []
    if length == 0:  # base case
        print(prefix)
        return
    for digit in range(base):  # recurrent case
        prefix.append(digit)
        generate_numbers(base, length - 1, prefix)
        prefix.pop()


generate_numbers(5, 5)
