package main

import "fmt"

// MergeSort divides the slice into two parts, sorts both the part of slice and then merge it
// Time complexity : O(size(log(size)))
// Space complexity : O(size)
func MergeSort(slice []int) []int {
	if len(slice) < 2 {
		return slice
	}
	mid := (len(slice)) / 2
	return merge(MergeSort(slice[:mid]), MergeSort(slice[mid:]))
}

// merge merges two sorted slice
// Time complexity : O(size)
// Space complexity : O(size)
func merge(left []int, right []int) []int {
	i := 0
	j := 0
	size := len(left) + len(right)
	slice := make([]int, size, size) // make built-in function allocates and initializes an object of type slice
	for k := 0; k < size; k++ {
		if i > len(left)-1 && j < len(right) {
			slice[k] = right[j]
			j++
		} else if j > len(right)-1 && i < len(left) {
			slice[k] = left[i]
			i++
		} else if left[i] < right[j] {
			slice[k] = left[i]
			i++
		} else {
			slice[k] = right[j]
			j++
		}
	}
	return slice
}

func main() {
	slice := []int{8, 2, 4, 9, 1, 699, 0, 9999}
	fmt.Println("Sorted data is:")
	slice = MergeSort(slice)
	fmt.Println(slice)
}
