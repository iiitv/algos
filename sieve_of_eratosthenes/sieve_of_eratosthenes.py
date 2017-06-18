import math


def sieve_of_eratosthenes(n):
    """
    Calculates prime numbers till a number n
    :param n: Number upto which to calculate primes
    :return: A boolean list contaning only primes
    """
    primes = [True] * (n + 1)  # Setting all as True initially
    primes[0] = primes[1] = False  # Since 0 and 1 are not primes
    sqrt_n = int(math.ceil(math.sqrt(n)))
    for i in range(2, sqrt_n, 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    return primes


def main():
    n = 425
    primes = sieve_of_eratosthenes(n)
    for i in range(n + 1):  # Printing primes
        if primes[i]:
            print(i)


if __name__ == '__main__':
    main()
