# Function to get no of set bits in binary 
# representation of positive integer n (iterative approach)
def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
  
  
# Program to test function countSetBits 
# std input would also work 
i = 9
print(countSetBits(i)) 

# contributed by
# Sampark Sharma
