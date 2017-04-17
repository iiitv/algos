def median(a, i, j, k):
    """
    Returns Median of 3 integers from array a.
    :param a: Iterable of elements
    :param i: index of element of set, whose meadian is to be returned
    :param j: index of element of set, whose meadian is to be returned
    :param k: index element of set, whose meadian is to be returned
    :return: returns the value of index median of a[i], a[j], a[k].
    """
    if a[i] > a[j]:
        return j if a[j] < a[k] else k
    else:
        return i if a[i] < a[k] else k


def partition(array, l, r):
    """
    Perform Partition Operation on array.
    Time Complexity: Theta(nLogn)
    Auxiliary Space: O(n)
    :param array: Iterable of elements
    :param l: left limit of array
    :param r: right limit of array
    :return: return q (partition index) value for function, used in partitioning of array.
    """
    i = l - 1
    pivot_index = median(array, l, r, (l + r) // 2)
    pivot = array[pivot_index]
    for j in range(l, r+1):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[r] = array[r], array[i]
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
