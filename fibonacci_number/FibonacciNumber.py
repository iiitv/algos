# This program uses Dynamic Programming and has space optimisation
# We keep changing the values of x and y


def fibonaaci(n):
    x = 0  # 0th fibonaaci number is 0
    y = 1  # 1st fibonaaci number is 1
    if n < 0:
        print ("Index can't be less than zero.")
    elif n == 0:
        return x  # 0th fibonaaci number
    elif n == 1:
        return y  # 1st fibonaaci number
    else:
        for i in range(2, n):

            # x and y are continously updated in the loop,
            # hence we don't have to create an array
            # and store all the values of fibonaaci numbers uptil n

            c = x + y  # current fibonaaci number is the sum of previous two fibonaaci numbers
            x = y  # setting the value of x equal to the value of (i-1)th fibonaaci numnber
            y = c  # setting the value of y equal to the ith fibonaaci number
        return y  # nth fibonaaci number


# Driver Program

f = int(input('Enter the value of the index : '))
print ('Fibonacci Number at Position ' + str(f) + ' is: ' \
    + str(fibonaaci(f)))  # prints the fth fibonaaci number

# Time Complexity : O(n)
