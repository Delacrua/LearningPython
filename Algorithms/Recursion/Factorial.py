def factorial(n: int) -> int:
    """
    The function returns factorial of given integer

    :param n: given integer
    :return: integer
    :raises AssertionError if given integer is negative
    """
    assert n >= 0, AssertionError('Function works for non-negative integers')
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(5))
