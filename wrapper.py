import time
def wrapper(func, *args, **kwargs):
    """
    The function is a decorator which serves for measuring the time that other functions require for computations
    :param func: the input function
    :param args: the input args
    :param kwargs: the input kwargs
    :return: modified function
    """
    start = time.time()
    result = func(*args, **kwargs)
    time_spent = time.time() - start
    return result, time_spent


fib_dict = {}
def rec_fib(n):
    if n in fib_dict:
        return fib_dict[n]
    elif n < 2:
        fib_dict[n] = n
    else:
        fib_dict[n] = rec_fib(n-1) + rec_fib(n-2)
    return fib_dict[n]


print(wrapper(rec_fib, 699))
