def fast_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return fast_pow(a, n - 1) * a
    else:
        return fast_pow(a**2, n//2)

print(fast_pow(2, 8))

