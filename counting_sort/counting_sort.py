def countOccurences(a, c):
    for i in range(len(a)):
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] = c[i - 1] + c[i]


def countingSort(a, k):
    b = [0] * len(a)
    c = [0] * (k + 1)
    countOccurences(a, c)
    for i in range(len(a) - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
    return b


def main():
    A = [3, 4, 5, 3, 6, 3, 3, 5, 5, 3, 2, 1, 5, 8]
    k = 0
    for i in range(len(A)):
        if k < A[i]:
            k = A[i]
    A = countingSort(A, k)
    print
    A


if __name__ == '__main__':
    main()
