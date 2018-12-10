from math import sqrt
import sys

def f(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(f(n))