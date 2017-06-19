def coin_change_problem(coins, amount):
    """
    Find out maximum number of ways in which a amount can
    be obtained using fixed value coins.

    Time Complexity : O((type of coins)*amount)
    :param coins: Iterable of elements containing value of coins.
    :param amount: It is value which is to be obtained with coins.
    :return: returns maximum number of ways amount can be arranged in.
    """
    possibilities = [0] * (amount + 1)
    possibilities[0] = 1
    for i in coins:
        for j in range(i, amount + 1):
            possibilities[j] += possibilities[j - i]
    return possibilities[amount]


def main():
    coins = [1, 2, 5]
    amount = 10
    print(coin_change_problem(coins, amount))


if __name__ == '__main__':
    main()
