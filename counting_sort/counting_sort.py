def count_occurences(a, c):
    for i in a:
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] = c[i - 1] + c[i]


def counting_Sort(a, k):
    b = [0] * len(a)
    c = [0] * (k + 1)
    countOccurences(a, c)
    for i in range(len(a) - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
    return b


def main():
    A = [3, 4, 5, 3, 6, 3, 3, 5, 5, 3, 2, 1, 5, 8]
    k = max(A)
    print(counting_sort(A, k))


if __name__ == '__main__':
    main()
