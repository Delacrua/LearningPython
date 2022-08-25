"""
Case 1: simple recursive algorithm
"""


def find_gcd_subtraction(a: int, b: int) -> int:
    """
    The function returns the greatest common divisor of two integers using Euclidean algorithm based on subtraction
    """
    if a == b:
        return a
    elif a > b:
        return find_gcd_subtraction(a - b, b)
    else:
        return find_gcd_subtraction(a, b - a)


"""
Case 2: advanced recursive algorithm
"""


def find_gcd_division(a: int, b: int) -> int:
    """
    The function returns the greatest common divisor of two integers using Euclidean algorithm based on division
    """
    return a if b == 0 else find_gcd_division(b, a % b)


print(find_gcd_subtraction(415, 35))
print(find_gcd_division(415623234, 36))
