def rod_cutting(price, n):
    """
    Computes maximum money that can be earned by cutting
    a rod of length n (Bottom-Up Approach).

    Time Complexity : O(n^2)
    Space Complexity : O(n)
    :param price: List in which price[i] denotes price of rod of length i.
    :param opt_price: List whose ith element is solution for rod of length i.
    :param n: Total length of rod to be considered for optimal amount.
    :param max_val: This variable is temporary optimal price.
    :return: returns optimal solution for rod of length n.
    """
    opt_price = [0]*(n+1)

    for i in range(1, n+1):
        max_val = -1
        for j in range(i):
            max_val = max(max_val, price[j] + opt_price[i-j-1])
        opt_price[i] = max_val
    return opt_price[n]


def main():
    """
    Main Function of this program.

    :param price: List in which price[i] denotes price of rod of length i.
    :param rod_length : Length for rod, whose optimal solution is needed.
    """
    price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    rod_length = 4
    print(rod_cutting(price, rod_length))


if __name__ == '__main__':
    main()
