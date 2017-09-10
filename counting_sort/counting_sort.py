#  Running time Complexity: O(z) where z = max(len(array), max(array))
#  Auxillary Space: O(n)


def count_occurences(array, count_array):
    """
    :param array: iterable of elements
    :param count_array: Intermediate variable
    Time Complexity: O(n)
    """
    for i in array:
        count_array[i] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]


def counting_sort(array, max_value):
    """
    :param array: Iterable of elements
    :param max_value: Maximum value in array
    :return: Sorted array
    """
    b = [0] * len(array)
    count_array = [0] * (max_value + 1)
    count_occurences(array, count_array)
    for i in range(len(array) - 1, -1, -1):
        b[count_array[array[i]] - 1] = array[i]
        count_array[array[i]] -= 1
    return b


def main():
    array = [3, 4, 5, 3, 6, 3, 3, 5, 5, 3, 2, 1, 5, 8]
    max_value = max(array)
    print(counting_sort(array, max_value))


if __name__ == '__main__':
    main()
