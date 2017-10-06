def median(a, i, j, k):
    """
    Return median of 3 integers from array a.
    :param a: Iterable of elements
    :param i: start element index
    :param j: end element index
    :param k: middle element index
    :return: return median of values at indices i, j and k.
    """
    ai, aj, ak = a[i], a[j], a[k]
    med_val = ai + aj + ak - max(ai, aj, ak) - min(ai, aj, ak)
    if ai == med_val:
        return i
    elif aj == med_val:
        return j
    return k


def partition(array, l, r):
    """
    Perform Partition Operation on array.
    Time Complexity: Theta(nLogn)
    Auxiliary Space: O(n)
    :param array: Iterable of elements
    :param l: pivot value for array
    :param r: right limit of array
    :return: return q value for function, used in partitioning of array.
    """
    i = l - 1
    pivot_index = median(array, l, r, (l+r) // 2)
    array[pivot_index], array[r] = array[r], array[pivot_index]
    pivot = array[r]
    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[r], array[i] = array[i], array[r]
    return i


def quick_sort(array, left, right):
    """
    Perform sort using partition function.
    Time Complexity : O(nlog(n)).
    Space Complexity : O(n).
    :param array: Iterable of elements
    :param left: used as left limit of quick sort
    :param right: right limit for quick sort
    :return: no returns, sorts array
    """
    if left < right:
        q = partition(array, left, right)
        quick_sort(array, left, q - 1)
        quick_sort(array, q + 1, right)


def main():
    a = [1, 2, 1, 2, 3, 1, 2, 2, 1]
    quick_sort(a, 0, len(a) - 1)
    print(a)


if __name__ == '__main__':
    main()
