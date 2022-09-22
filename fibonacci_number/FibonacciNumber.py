# fibonacci function return the nth fibonacci no for all n>0
def fibonacciNumber(n):
    if n==1 or n==2:
        return n-1
    
    a, b, fib = 0, 1, 0
    for i in range(2, n):
        fib = a+b
        a,b = b,fib
    
    return fib
    
#Main

n = 5
print(fibonacciNumber(10))
