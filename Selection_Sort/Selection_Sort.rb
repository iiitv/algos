# passing array in SelectionSort fuction 
def SelectionSort(a)
  # n is a variable which holds the  length of array which we can be find  by using inbuilt 'length' function
  n = a.length - 1  
  i = 0
  while i <= n - 1
    #smallest variable will hold the smallest value
    smallest = i
    j = i + 1
    while j <= n
      smallest = j if a[j] < a[smallest]
      j += 1
    end
    #swap
    a[i], a[smallest] = a[smallest], a[i] if i != smallest 
    i += 1
  end
end

#declare array 
# a is name of array and inbuilt function 'shuffle'will shuffle the values of array a
a = ([89,55,101,36].shuffle)

#calling SelectionSort function
SelectionSort(a)

#print the sorted array
puts "Sorted array is: #{a.inspect}"
