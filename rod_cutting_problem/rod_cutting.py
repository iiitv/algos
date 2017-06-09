"""
    This module calculates optimized solution for rod cutting
    by function rod_cutting() with arguments as defined
    in main()
"""


def rod_cutting(price, rod_len):
    """
    Computes maximum money that can be earned by cutting
    a rod of length rod_len (Bottom-Up Approach).

    Time Complexity : O(rod_len^2)
    Space Complexity : O(rod_len)
    :param price: List in which price[i] denotes price of rod of length i.
    :param rod_len: Total length of rod to be considered for optimal amount.
    :return: returns optimal solution for rod of length rod_len.
    """
    opt_price = [0] * (rod_len + 1)

    for i in range(1, rod_len + 1):
        max_val = -1
        for j in range(i):
            max_val = max(max_val, price[j] + opt_price[i - j - 1])
        opt_price[i] = max_val
    return opt_price[rod_len]


def main():
    """
    Main Function of this program.
    """
    price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    rod_length = 4
    print(rod_cutting(price, rod_length))


if __name__ == '__main__':
    main()
