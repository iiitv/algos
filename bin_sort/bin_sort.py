"""
Following is the implementation of bin sort algorithm.
It will sort the input array with time complexity H(N + K)
N being the size of array, K being the number of buckets.
Space complexity is at worst O(NK).
"""


import math


def insertion_sort(a):
    """
    :param a: list
        List of objects with an order
    :return: list
        Sorted list with insertion sort algorithm
    """

    for i in range(1, len(a)):
        current_value = a[i]
        position = i

        while position > 0 and a[position - 1] > current_value:
            a[position] = a[position - 1]
            position -= 1
            a[position] = current_value

    return a


def get_buckets(a, bucket_size):
    """
    :param a: list
        List of objects with an order
    :param bucket_size: int
        Size of buckets to fill
    :return: list
        List of buckets to sort array with
    """

    min_v, max_v = min(a), max(a)  # min and max values in array
    bucket_count = int(math.floor((max_v - min_v) / bucket_size)) + 1
    buckets = [[] for _ in range(bucket_count)]  # initialize buckets
    for x in a:  # distribute values into buckets
        buckets[
            int(math.floor((x - min_v) / bucket_size))
        ].append(x)
    return buckets


def bin_sort(a, bucket_size=16):
    """
    :param a: list
        List of objects with an order
    :param bucket_size: int
        Size of buckets to fill
    :return: list
        Sorted list with bin sort algorithm
    """

    if len(a) == 0:  # trivial case
        return a

    buckets = get_buckets(a, bucket_size)  # get buckets
    a = []
    for i in range(0, len(buckets)):  # sort each bucket ...
        buckets[i] = insertion_sort(buckets[i])  # insertion sort

        for x in buckets[i]:  # ... and place back into array
            a.append(x)

    return a


def main():
    """
    :return: void
        Sorts sample list with bin sort algorithm,
        then prints sorted list
    """

    unsorted_list = [
        437230, 851821, 184681, 173673, 13306, 768361, 431982, 956700, 65143,
        556681, 198208, 983511, 170469, 313978, 552536, 334818, 527289,
        959491, 303675, 532988
    ]

    sorted_list = bin_sort(unsorted_list)
    print(sorted_list)


if __name__ == '__main__':
    main()
