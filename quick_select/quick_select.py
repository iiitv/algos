def partition(array, start, end):
    """
    Perform Partition Operation on array a.
    Time Complexity: O(nLogn)
    Auxiliary Space: O(n)
    :param a: Iterable of elements
    :param start: pivot value for array
    :param end: right limit of array
    :return: return i value for function, used in partitioning of array.
    """
    i = start - 1
    pivot = array[end]
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[end] = array[end], array[i]
    return i


def quick_select(array, k):
    """
    Perform quick select operation i.e find kth minimum element from array
    Time Complexity: O(n) for average case and O(n^2) for worst cases
    param a: Array on which operation would perfom
    param k: kth minimun element have to find
    return: returns kth minimum value
    """
    start = 0
    end = len(array) - 1
    is_found = False
    while not is_found:
        pos = partition(array, start, end)
        if pos == k:
            is_found = True
            return array[pos]
        elif pos < k:
            start = pos + 1
        else:
            end = pos - 1


def main():
    a = [2, 4, 6, 2, 1, 4, 2, 7, 8, 9, 5, -4, 23, 0, 8]
    k = 10
    if a is None:
        print("Array doesn't exist")
    elif k >= len(a):
        print("k is greater than size of array")
    else:
        print(quick_select(a, k))


if __name__ == '__main__':
    main()
