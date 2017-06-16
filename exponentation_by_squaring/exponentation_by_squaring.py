def exponentation_by_squaring(base, power):
    """
    Calculates base ^ power using recursion, efficient algorithm to inbuilt pow() function
    :param base: Base of expression
    :param power: Power of expression
    :return: returns base ^ power
    """

    if power < 0:  # Negative powers
        return exponentation_by_squaring(1. / base, -power)
    elif power == 0:  # Base case
        return 1
    elif power % 2 == 0:
        return exponentation_by_squaring(base * base, power // 2)
    elif power % 2 == 1:
        return base * exponentation_by_squaring(base * base, (power - 1) // 2)


def main():
    """
    driver function to calculate base ^ power
    """

    base = 2
    power = 3
    print(str(base) + ' raised to ' + str(power) + ' is ' +
          str(exponentation_by_squaring(base, power)))


if __name__ == '__main__':
    main()
