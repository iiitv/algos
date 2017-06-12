"""
Following is the implementation of heap_sort algorithm.
It will sort the input array with time complexity O(N*logN)
N being the size of array.
Space complexity is O(1).
"""


def left_child_index(i):
    """
    :param i: int
        Index of node in array (that is organized as heap)
    :return: int
        Position in array of left child of node
    """

    return 2 * (i + 1) - 1


def right_child_index(i):
    """
    :param i: int
        Index of node in array (that is organized as heap)
    :return: int
        Position in array of right child of node
    """

    return left_child_index(i) + 1


def get_children_of_node(a, i):
    """
    :param a: list
        List organized as heap, i.e for each node i:
            left children is at position 2(i + 1) - 1
            right children is at position 2(i + 1))
    :param i: int
        Index of parent node in array (that is organized as heap)
    :return: (left children index, left children node) and
        (right children index, right children node)
    """

    l = left_child_index(i)  # index and value of children
    l_val = a[l] if 0 <= l < len(a) else None
    r = right_child_index(i)
    r_val = a[r] if 0 <= r < len(a) else None
    return (l, l_val), (r, r_val)


def find_largest_in_family(a, i):
    """
    :param a: list
        List organized as heap, i.e for each node i:
            left children is at position 2(i + 1) - 1
            right children is at position 2(i + 1))
    :param i: int
        Index of parent node in array (that is organized as heap)
    :return: index of largest value among parent and children
    """

    (l, l_val), (r, r_val) = get_children_of_node(a, i)
    largest_i = i  # find index of largest value among a[i] and its children
    if l_val is not None and l_val > a[i]:
        largest_i = l

    if r_val is not None and r_val > a[largest_i]:
        largest_i = r

    return largest_i


def max_heapify(a, i):
    """
    :param a: list
        List organized as heap, i.e for each node i:
            left children is at position 2(i + 1) - 1
            right children is at position 2(i + 1))
    :param i: int
        Index of array where to start checking for max-heap condition from
    :return: list
        List organized as max-heap.
    """

    largest_i = find_largest_in_family(a, i)  # find largest node
    if largest_i != i:  # swap only if it's needed
        a[largest_i], a[i] = a[i], a[largest_i]  # swap
        return max_heapify(a, largest_i)

    return a


def heap_sort(a):
    """
    :param a: list
        List of objects with an order
    :return: list
        Sorted list with heap sort algorithm
    """

    for i in range(len(a) // 2, 0, -1):
        a = max_heapify(a, i)  # create max-heap

    for i in range(len(a) // 2, 0, -1):
        a[0], a[i] = a[i], a[0]  # swap first and last item
        a = max_heapify(a, i)

    return a


def main():
    """
    :return: void
        Sorts sample list with heap sort algorithm,
        then prints sorted list
    """

    unsorted_list = [
        437230, 851821, 184681, 173673, 13306, 768361, 431982, 956700, 65143,
        556681, 198208, 983511, 170469, 313978, 552536, 334818, 527289,
        959491, 303675, 532988
    ]

    sorted_list = heap_sort(unsorted_list)
    print(sorted_list)


if __name__ == '__main__':
    main()
