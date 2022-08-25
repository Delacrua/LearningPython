def fast_pow(a: int, n: int) -> int:
    """
    The function takes a number a and takes its power of n using fast recursive algorithm

    :param a: given non-negative number
    :param n: power of given number
    :return: integer
    """
    assert a >= 0 and n >= 0, AssertionError('The function requires non-negative numbers '
                                             'to be passed as arguments')
    if n == 0:
        return 1
    elif n % 2 != 0:
        return fast_pow(a, n - 1) * a
    else:
        return fast_pow(a ** 2, n // 2)


print(fast_pow(2, 64))

