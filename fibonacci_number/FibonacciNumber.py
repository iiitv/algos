"""
Calculates and returns the nth fibonacci number
"""
def fibonacci(n):
    if n==1: # first number of fibonacci
        return 0
    elif n==2: # second number of fibonacci
        return 1
    else:
        a,b=0,1 # a is the previous number (0) and b is the current number (1)
        for i in range(2,n): # starts with the third number of fibonacci
            a,b=b,a+b # assign current number to a and sum of previous and current to b
        return b

def main():
    L=[1,2,5,10,15]
    for n in L:
        if n<=0: # input must be greater than or equal to 1
            print("Enter a valid number")
        else:
            print(fibonacci(n)) # Output of fibonacci

if __name__ == "__main__":
    main()
