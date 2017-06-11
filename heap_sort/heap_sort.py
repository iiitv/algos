"""
Following is the implementation of heap_sort algorithm.
It will sort the input array with time complexity O(N*logN)
N being the size of array.
Space complexity is O(1).
"""


def left_child_index(i):
    """
    :param i: int
        Index of node in array (that is organised as heap)
    :return: int
        Position in array of left child of node
    """

    return 2 * (i + 1) - 1


def get_left_child(a, i):
    """
    :param a: list
        List organized as heap
    :param i: int
        Index of node in array (that is organised as heap)
    :return: object
        Value of left child of node
    """

    child_i = left_child_index(i)
    if child_i in range(len(a)):
        return a[child_i]
    else:
        return None


def right_child_index(i):
    """
    :param i: int
        Index of node in array (that is organised as heap)
    :return: int
        Position in array of right child of node
    """

    return left_child_index(i) + 1


def get_right_child(a, i):
    """
    :param a: list
        List organized as heap
    :param i: int
        Index of node in array (that is organised as heap)
    :return: object
        Value of left child of node
    """

    child_i = right_child_index(i)
    if child_i in range(len(a)):
        return a[child_i]
    else:
        return None


def max_heapify(a, i):
    """
    :param a: list
        List organized as heap (i.e for each node i, left children is at position 2(i + 1) - 1 and the right children is at position 2(i + 1))
    :param i: int
        Index of array where to start checking for maxheap condition from
    :return: list
        List organized as maxheap.
    """

    l, l_val = left_child_index(i), get_left_child(a, i)  # position and value fo children
    r, r_val = right_child_index(i), get_right_child(a, i)

    largest_i = i  # find index of smallest value among a[i] and its children
    if l_val is not None and l_val > a[i]:
        largest_i = l
    if r_val is not None and r_val > a[largest_i]:
        largest_i = r

    if largest_i != i:
        a[largest_i], a[i] = a[i], a[largest_i]  # swap
        return max_heapify(a, largest_i)

    return a


def heap_sort(a):
	"""
	:param a: list
		List of objects with an order
	:return: list
        Sorted list with heap_sort algorithm
	"""

	for i in range(int(len(a) / 2), 0, -1):
		a = max_heapify(a, i)  # create maxheap

	for i in range(int(len(a) / 2), 0, -1):
		a[0], a[i] = a[i], a[0]  # swap first and last item
		a = max_heapify(a, i)

	return a

if __name__ == '__main__':
	unsorted_list = [437230, 851821, 184681, 173673, 13306, 768361, 431982, 956700, 65143, 556681, 198208, 983511, 170469, 313978, 552536, 334818, 527289, 959491, 303675, 532988]
	sorted_list = heap_sort(unsorted_list)
	print(sorted_list)
