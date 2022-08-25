def get_primes(num: int) -> list:
    """
    The function takes an integer and returns a list of primes in range [2, integer + 1) using Sieve of Eratosthenes
    :param num: input integer
    :return: list of corresponding primes
    """
    primes = list(range(2, num + 1))
    for number in primes:
        i = 2
        while number * i <= primes[-1]:
            if number * i in primes:
                primes.remove(number * i)
            i += 1
    return primes


print(get_primes(100))
