import math


def sieve_of_erastosthenes(n):
    """
    Calculates prime numbers till a number n
    :param n: Number upto which to calculate primes
    :param primes: A boolean List having all entries True
    :return: A boolean list contaning only primes
    """
    primes = [True for i in range(n+1)]    # Setting all as True initially
    primes[0] = primes[1] = False    # Since 0 and 1 are not primes
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n+1):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
        i += 1
    return primes


def main():
    n = int(input())
    primes = sieve_of_erastosthenes(n)
    for i in range(n+1):    # Printing primes
        if primes[i]:
            print(i)


if __name__ == '__main__':
    main()
