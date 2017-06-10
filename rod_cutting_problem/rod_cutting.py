"""
    This module calculates optimized solution for rod cutting
    by function rod_cutting() with arguments as defined
    in main()
"""


def rod_cutting(price):
    """
    Computes maximum money that can be earned by cutting
    a rod of length len(price) (Bottom-Up Approach).

    Time Complexity : O((len(price))^2)
    Space Complexity : O(len(price))
    :param price: List in which price[i] denotes price of rod of length i.
    :return: returns optimal solution for rod of length len(price).
    """
    length = len(price)
    opt_price = [0] * (length + 1)

    for i in range(1, length + 1):
        opt_price[i] = max(
                    [-1] + [price[j] + opt_price[i - j - 1] for j in range(i)])
    return opt_price[length]


def main():
    """
    Main Function of this program.
    """
    price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(rod_cutting(price))


if __name__ == '__main__':
    main()
