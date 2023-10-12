def recursive_fibonacci(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.

    :param n: The index of the Fibonacci number to calculate.
    :return: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def iterative_fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.

    :param n: The index of the Fibonacci number to calculate.
    :return: The nth Fibonacci number.
    """
    previous_1 = 0
    previous_2 = 1
    
    for i in range(n):
        current = previous_1 + previous_2
        previous_1 = previous_2
        previous_2 = current
    
    return previous_1

def main():
    """
    Main function to take user input and display the Fibonacci number.
    """
    print("Choose a Fibonacci calculation method:")
    print("1. Recursive")
    print("2. Iterative")
    
    choice = int(input("Enter your choice (1 or 2): "))
    n = int(input("Enter the index of the Fibonacci number: "))
    
    if n <= 0:
        print("Please enter a valid index greater than zero.")
    else:
        if choice == 1:
            print("Fibonacci number at index", n, "is:", recursive_fibonacci(n))
        elif choice == 2:
            print("Fibonacci number at index", n, "is:", iterative_fibonacci(n))
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == '__main__':
    main()
