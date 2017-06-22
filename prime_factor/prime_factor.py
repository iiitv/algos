import math


def prime_factor(num):
    """
    Finds all the prime factor of a number.

    :param num : number whose prime factors we want to find.
    :return : return a list of prime factors of number.
    """
    factor_list = []
    sqrt_num = int(math.sqrt(num)) + 1
    for start in range(2, sqrt_num):
        if num % start == 0:
            factor_list.append(start)
            while (num % start == 0):
                num /= start
    if num != 1:
        factor_list.append(num)
    return factor_list


def main():
    """
    Driver function
    """
    num = 362880
    print("Prime Factors are :", prime_factor(num))


if __name__ == '__main__':
    main()
