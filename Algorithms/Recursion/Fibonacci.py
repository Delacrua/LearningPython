from functools import lru_cache

"""
Case 1: simple recursive function
"""


def fib_rec(n: int) -> int:
    """
    The function returns n's Fibonacci number using recurrence relation
    """
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


"""
Case 2: recursive function with simple previous values storage
"""
fib_dict = {}


def fib_rec_with_dict(n: int) -> int:
    if n in fib_dict:
        return fib_dict[n]
    elif n == 0:
        fib_dict[n] = 0
    elif n <= 2:
        fib_dict[n] = 1
    else:
        fib_dict[n] = fib_rec_with_dict(n - 1) + fib_rec_with_dict(n - 2)
    return fib_dict[n]


"""
Case 3: recursive function with previous values caching with built-in decorator cache
"""


@lru_cache()
def fib_rec_cached(n: int) -> int:
    """
    The function returns n's Fibonacci number using recurrence relation and built-in caching decorator
    """
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib_rec_cached(n - 1) + fib_rec_cached(n - 2)


print('recurrent fibonacci')
print(fib_rec(1))
print(fib_rec(2))
print(fib_rec(32))
print('recurrent fibonacci with data storage')
print(fib_rec_with_dict(1))
print(fib_rec_with_dict(2))
print(fib_rec_with_dict(32))
print(fib_rec_with_dict(100))
print('recurrent fibonacci with cache')
print(fib_rec_cached(1))
print(fib_rec_cached(2))
print(fib_rec_cached(32))
print(fib_rec_with_dict(100))
