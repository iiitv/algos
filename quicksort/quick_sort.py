def partition(array, p, r):
    """
    Perform Partition Operation on array.
    Time Complexity: Theta(nLogn)
    Auxiliary Space: O(n)
    :param array: Iterable of elements
    :param p: pivot value for array
    :param r: right limit of array
    :return: return q value for function, used in partitioning of array.
    """
    i = p - 1
    pivot = array[r]
    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[r], array[i] = array[i], array[r]
    return i


def quick_sort(array, pivot, right):
    """
    Perform sort using partition function.
    Time Complexity : O(nlog(n)).
    Space Complexity : O(n).
    :param array: Iterable of elements
    :param pivot: used as left limit of quick sort
    :param right: right limit for quick sort
    :return: no returns, sorts array
    """
    if pivot < right:
        q = partition(array, pivot, right)
        quick_sort(array, pivot, q - 1)
        quick_sort(array, q, right)


def main():
    a = [15, 19, 18, 26, 456, 87, 45, 480, 5]
    quick_sort(a, 0, len(a) - 1)
    print(a)

if __name__ == '__main__':
    main()
