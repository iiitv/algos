import math


def prime_factor(num):
    """

    Prime factor of a number


    :param start : checking number if it is a prime factor of number entered
    :param counter : checking the number of factors of start
    :param checker : checks if start is a prime number or not
    :return : no returns
    """
    print("Factors are:")
    start = 1
    while start <= num:
        counter = 0
        if num % start == 0:
            checker = 1
            while checker <= math.sqrt(start):
                if start % checker == 0:
                    counter += 1
                checker += 1
            if counter == 2:
                print(start)
        start += 1


def main():
    """
    Driver function
    """
    num = 1255
    prime_factor(num)


if __name__ == '__main__':
    main()
