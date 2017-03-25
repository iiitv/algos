import random


def binary_search(array, element):
    """
    Performs Binary Search by Iterative Method
    :param array: Iterable of elements
    :param element: element to search
    :return: returns value of index of element (if found) else return None
    """
    left = 0
    right = len(array)
    while left <= right:
        mid = int((right + left) / 2)
        # indices of a list must be integer
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return None


def binary_search_recursive(array, left, right, element):
    """
    Performs Binary Search by Iterative Method
    :param array: Iterable of elements
    :param left: start limit of array
    :param right: end limit of array
    :param element: element to be searched
    :return: returns value of index of element (if found) else return None
    """
    if right >= left:
        mid = int(left + (right - left) / 2)
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            return binary_search_recursive(array, left, mid - 1, element)
        else:
            return binary_search_recursive(array, mid + 1, right, element)
    else:
        return None


def main():
    size = 100  # user can change it
    domain = 100  # user can change it
    array = [random.randint(0, domain) for i in range(size)]
    # print ("Array :", array)
    array.sort(key=int)
    # print ("Sorted Array :", array)
    element = random.randint(0, domain)
    # i.e. a random element can be selected from domain
    print('Element = ', element)
    length = len(array)
    result = binary_search_recursive(array, 0, length - 1, element)
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
