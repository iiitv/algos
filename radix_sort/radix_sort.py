# Following is the implementation of Radix Sort.


def radix_sort(arr, radix=10):
    """
    :param arr: Iterable of elements to sort.
    :param radix: Base of input numbers
    :return: Sorted list of input.
    Time complexity: O(d * (n + b))
    where, n is the size of input list.
           b is base of representation.
           d is number of digits in largest number in that base.
    Space complexity: O(n + k)
    where, k is the range of input.
    """
    max_length = False
    tmp, digit = -1, 1

    while not max_length:
        max_length = True
        # declare and initialize buckets
        buckets = [[] for _ in range(radix)]

        # split arr between lists
        for i in arr:
            tmp = i // digit
            buckets[tmp % radix].append(i)
            if max_length and tmp > 0:
                max_length = False

        # empty lists into arr array
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1

        # move to next digit
        digit *= radix
    return arr


def main():
    """
    Driver function to test radix sort.
    """
    test = [170, 45, 75, 90, 802, 24, 2, 66]
    print('Sorted array:', radix_sort(test))


if __name__ == '__main__':
    main()
