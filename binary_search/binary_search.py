from random import randint

def binarySearchIterative (array, left, right, element):
    while left <= right:
        mid = int(left + (right - left)/2);  # indices of a list must be integer
        if array[mid] == element:
            return mid
 
        elif array[mid] < element:
            left = mid + 1

        else:
            right = mid - 1
     
    return -1

def binarySearchRecursive (array, left, right, element):
    if right >= left:
        mid = int(left + (right - left)/2) 	# indices of a list must be integer 
        if array[mid] == element:
            return mid
      
        elif array[mid] > element:
            return binarySearchRecursive(array, left, mid-1, element)
 
        else:
            return binarySearchRecursive(array, mid+1, right, element)
 
    else:
        return -1

def main():
  size = 100  		# user can change it
  domain = 100		# user can change it
  array = [randint(0, domain) for i in range(size)]
  #print ("Array :", array)
  array.sort(key = int)
  #print ("Sorted Array :", array)
  element = randint(0, domain)   # i.e. a random element can be selected from domain
  print ("Element = ", element)
  length = len (array)
  result = binarySearchRecursive (array, 0, length-1, element)
  if result != -1:
      print ("Recursive Binary Search : Element is present at index",result)
  else:
	    print ("Recursive Binary Search : Element is not present in array")
  
  result = binarySearchIterative (array, 0, length-1, element)
  if result != -1:
      print ("Iterative Binary Search : Element is present at index",result)
  else:
	    print ("Iterative Binary Search : Element is not present in array")
	    
if __name__ == '__main__':
    main()
