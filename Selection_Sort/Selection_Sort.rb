def SelectionSort(a)# passing array in SelectionSort fuction 
  n = a.length - 1# n is a variable which holds the  length of array which we can be find  by using inbuilt 'length' function  
  i = 0
  while i <= n - 1
    smallest = i#smallest variable will hold the smallest value
    j = i + 1
    while j <= n
      smallest = j if a[j] < a[smallest]
      j += 1
    end
    a[i], a[smallest] = a[smallest], a[i] if i != smallest #swap
    i += 1
  end
end

#declare array 
a = ([89,55,101,36].shuffle)# a is name of array and inbuilt function 'shuffle'will shuffle the values of array a

SelectionSort(a)#calling SelectionSort function

puts "Sorted array is: #{a.inspect}"#print the sorted array
