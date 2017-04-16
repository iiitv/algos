def merge(array, left, right):
    """
    Perform Merge Operation between arrays.

    :param array: Iterable of elements
    :param left: left limit for merge sort
    :param right: right limit for merge sort
    :return: no returns, merges arrays.
    """
    mid = int((left + right )/ 2)
    s1 = int(mid - left + 1)
    s2 = int(right - mid)
    l = [0] * s1
    r = [0] * s2
    for i in range(s1):
        l[i] = array[int(left + i)]

    for j in range(s2):
        r[j] = array[mid + 1 + j]

    i = j = int(0)
    k = int(left)
    while(i < s1 and j < s2):
        if(l[i] <= r[j]):
            array[k] = l[i]
            i = i + 1
        else:
            array[k] = r[j]
            j = j + 1

        k = k + 1

    while(i < s1):
        array[k] = l[i]
        k = k + 1
        i = i + 1

    while(j < s2):
        array[k] = r[j]
        k = k + 1
        j = j + 1


def sort(array, left, right):
	"""
    Perform Merge Sort.

    :param array: Iterable of elements
    :param left: left limit for merge sort
    :param right: right limit for merge sort
    :return: no returns, sorts array
   	"""
	if(left < right):
		mid = int((left + right) / 2)
		sort(array, left, mid)
		sort(array, mid + 1, right)
		merge(array, left, right)

def main():
    a = [15, 19, 18, 26, 456, 87, 45]
    sort(a, 0, len(a) - 1)
    print(a)

if __name__ == '__main__':
	main()
