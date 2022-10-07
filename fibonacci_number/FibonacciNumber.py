def fib(n):
    if(n <= 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

print("Enter the number :")
t = int(input())
if(t == 0):
    print("Enter correct number!")
else:
        
    for i in range(t):
        x = fib(i)
    print("fibonacci number is :")
    print(x)