def insertionSort(alist):
    """
    Performs a insertion sort
    :type alist: object
    """
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1
            alist[position] = current_value


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(alist)


if __name__ == '__main__':
    main()
