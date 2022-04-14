import time
def wrapper(func, n):
    start = time.time()
    result = func(n)
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
