def nextPowOf2(n):
    p = 1
    if (n and not(n & (n - 1))):
        return n
    while (p < n) :
        p <<= 1
    return p;

t = int(input())
for i in range(t):
    n= int(input())
    print("Next Power of 2 " + str(nextPowOf2(n)))
