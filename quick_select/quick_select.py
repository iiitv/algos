def partition(a, start, end):
    """
    Perform Partition Operation on array a.
    Time Complexity: o(nLogn)
    Auxiliary Space: O(n)
    :param a: Iterable of elements
    :param start: pivot value for array
    :param end: right limit of array
    :return: return i value for function, used in partitioning of array.
    """
    i = start - 1
    pivot = a[end]
    for j in range(start, end):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[end] = a[end], a[i]
    return i


def quick_select(a, k):
    """
    Perform quick select operation i.e find kth minimum element from array
    Time Complexity: O(n) for average case and O(n^2) for worst cases
    param a: Array on which operation would perfom
    param k: kth minimun element have to find
    return: returns kth minimum value
    """
    if a is not None and len(a) >= k:
        start = 0
        end = len(a) - 1
        is_found = False
        while not is_found :
            pos = partition(a, start, end)
            if pos == k:
                is_found = True
                return a[pos]
            elif pos < k:
                start = pos + 1
            else:
                end = pos - 1
    else:
    	return None

def main():
    a = [2, 4, 6, 2, 1, 4, 2, 7, 8, 9, 5, -4, 23, 0, 8]
    k = 10
    ans = quick_select(a, k)
    if a is None:
        print ("Array doesn't exist")
    elif ans is not None:
        print (ans)
    else:
        print ("k is greater than size of array")


if __name__ == '__main__':
    main()
