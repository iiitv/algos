def merge(array, left, right):
    """
    Perform Merge Operation between arrays.
    Time Complexity: Theta(nLogn)
    Auxiliary Space: O(n)
    :param array: Iterable of elements
    :param left: left limit for merge sort
    :param right: right limit for merge sort
    :return: no returns, merges arrays.
    """
    mid = (left + right) // 2
    l = array[left:mid + 1]
    r = array[mid + 1:right + 1]
    k = left
    while l and r:
        if l[0] < r[0]:
            array[k] = l.pop(0)
        else:
            array[k] = r.pop(0)
        k += 1
    while l:
        array[k] = l.pop(0)
        k += 1
    while r:
        array[k] = r.pop(0)
        k += 1


def merge_sort(array, left, right):
    """
    Perform sort using merge function.
    Time Complexity : O(nlog(n)).
    Space Complexity : O(n).
    :param array: Iterable of elements
    :param left: left limit for merge sort
    :param right: right limit for merge sort
    :return: no returns, sorts array
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, right)


def main():
    a = [15, 19, 18, 26, 456, 87, 45, -1, 558897984]
    merge_sort(a, 0, len(a) - 1)
    print(a)


if __name__ == '__main__':
    main()
