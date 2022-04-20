import time


def decorator(func):
    start = time.perf_counter()

    def wrapper(*args, **kwargs):
        """
        The function is a decorator which serves for measuring the time that other functions require for computations
        :param args: the input args
        :param kwargs: the input kwargs
        :return: modified function
        """
        result = func(*args, **kwargs)
        return result

    print(f'Время работы алгоритма: {time.perf_counter() - start} секунд')
    return wrapper


fib_dict = {}


@decorator
def rec_fib(n):
    if n in fib_dict:
        return fib_dict[n]
    elif n < 2:
        fib_dict[n] = n
    else:
        fib_dict[n] = rec_fib(n - 1) + rec_fib(n - 2)
    return fib_dict[n]


print(rec_fib(499))
