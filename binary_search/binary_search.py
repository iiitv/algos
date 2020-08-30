from random import randint


def binary_search(array, element):
    """
    Perform Binary Search by Iterative Method.

    :param array: Iterable of elements
    :param element: element to search
    :return: returns value of index of element (if found) else return None
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        # indices of a list must be integer
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            right = mid - 1
        else:
            left = mid + 1
    return None


def binary_search_recursive(array, element, left=0, right=None):
    """
    Perform Binary Search by Iterative Method.

    :param array: Iterable of elements
    :param left: start limit of array
    :param right: end limit of array
    :param element: element to be searched
    :return: returns value of index of element (if found) else return None
    """
    right = len(array) - 1 if right is None else right
    if right >= left:
        mid = (right + left) // 2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            return binary_search_recursive(array, element, left, mid - 1)
        else:
            return binary_search_recursive(array, element, mid + 1, right)
    else:
        return None


def main():
    size = 100  # user can change it
    domain = 100  # user can change it
    array = [1, 9, 11, 13, 5, 7, 8, 5, 17, 1156, 114]
    array.sort()
    element = 13
    result = binary_search_recursive(array, element)
    if result is None:
        print('Recursive Binary Search : Element not present in array')
    else:
        print('Recursive Binary Search : Element is present at index', result)
    result = binary_search(array, element)
    if result is None:
        print('Iterative Binary Search : Element not present in array')
    else:
        print('Iterative Binary Search : Element is present at index', result)


if __name__ == '__main__':
    main()
