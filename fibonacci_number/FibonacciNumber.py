def series(n):
    """
    Find the first n Fibonacci Numbers.
    :param n: Nth elements of the fibonacci series.
    :return: returns None if n is 0 otherwise returns the list of first n fibonacci numbers.
    """
    if n==0:
        return None

    if n==1 or n==2:
        return n-1

    array = [0, 1]

    for i in range(2, n):
        array.append(array[i-1] + array[i-2])

    return array


def n_fib(n):
    """
    Find the nth Fibonacci Number.
    :param n: Nth element in the fibonacci series.
    :return: returns None if n is 0 otherwise returns the nth Fibonacci Number.
    """

    if n == 0:
        return None

    if n == 1 or n == 2:
        return n - 1

    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a+b

    return b


def main():
    n = int(input())

    result = series(n)
    if result is None:
        print("Enter number greater than 0")
    else:
        print("First n elements of fibonacci series is", result)

    result = n_fib(n)
    if result is None:
        print("Enter number greater than 0")
    else:
        print("The nth Fibonacci number is", result)

if __name__ == '__main__':
    main()