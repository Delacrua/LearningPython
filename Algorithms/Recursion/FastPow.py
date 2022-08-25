def fast_pow(integer: int, n: int) -> int:
    """
    The function takes an integer a and takes its power of n using fast recursive algorithm

    :param integer: given non-negative integer
    :param n: power of given integer
    :return: integer
    """
    assert integer >= 0 and n >= 0, AssertionError('The function requires non-negative integers '
                                                   'to be passed as arguments')
    if n == 0:
        return 1
    elif n % 2 != 0:
        return fast_pow(integer, n - 1) * integer
    else:
        return fast_pow(integer ** 2, n // 2)


print(fast_pow(2, 8))

