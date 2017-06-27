#Running time Complexity: O(z) where z = max(len(array), max(array))
#Auxillary Space: O(n)


def count_occurences(array, c):
	"""
	:param array: iterable of elements
	:param c: Intermediate variable
    :return: No returns, counts occurrences
    Time Complexity: O(n)
	"""
    for i in array:
        c[array] += 1
    for i in range(1, len(c)):
         c[i] += c[i - 1]


def counting_sort(array, k):
	"""
    :param array: Iterable of elements
    :param k: Max value
    :return: Output array
    """
    b = [0] * len(array)
    c = [0] * (k + 1)
    count_occurences(array, c)
    for i in range(len(array) - 1, -1, -1):
        b[c[array[i]] - 1] = array[i]
        c[array[i]] -= 1
    return b


def main():
    array = [3, 4, 5, 3, 6, 3, 3, 5, 5, 3, 2, 1, 5, 8]
    k = max(array)
    print(counting_sort(array, k))


if __name__ == '__main__':
    main()