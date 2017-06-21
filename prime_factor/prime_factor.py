import math


def prime_factor(num):
    """
    Finds all the prime factor of a number

    :param num : number whose prime factors we want to find  
    :return : return a list of prime factors of number
    """
    factor_list = []
    start = 1
    while start <= math.sqrt(num):
        counter = 0
        if num % start == 0:
            checker = 1
            while checker <= start:
                if start % checker == 0:
                    counter += 1
                checker += 1
            if counter == 2:
                factor_list.append(start)
        start += 1
    return factor_list


def main():
    """
    Driver function
    """
    num = 1255
    print("Prime Factors are :",prime_factor(num))


if __name__ == '__main__':
    main()
