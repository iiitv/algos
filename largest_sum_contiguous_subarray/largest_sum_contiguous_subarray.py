def largest_sum_contiguous_subarray(arr):
    """
    Find the subarray with maximum sum from all subarrays.

    :param arr: List of numbers to form subarray from.
    :return: The maximum sum in all subarrays.
    """
    max_now = 0
    max_next = 0
    for i in arr:
        max_next += i
        max_now = max(max_next, max_now)
        max_next = max(0, max_next)
    return max_now


def main():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print('Maximum contiguous sum is', largest_sum_contiguous_subarray(arr))


if __name__ == '__main__':
    main()
