def linear_search(arr, x):
    """
    Performs a linear search
    :param arr: Iterable of elements
    :param x: Element to search for
    :return: Index if element found else None
    """
    l = len(arr)
    for i in range(l):
        if arr[i] == x:
            return i
    return None


def main():
    arr = range(100)
    index = linear_search(arr, 55)
    if index is None:
        print('Element not found in array')
    else:
        print('Element found at index %s' % index)


if __name__ == '__main__':
    main()
