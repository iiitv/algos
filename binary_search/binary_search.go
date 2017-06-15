package main

import "fmt"

// BinarySearch perform Binary Search by Iterative Method.
// Time Complexity : O(log(len(array)))
func BinarySearch(array []int, target int) int {
	left, right := 0, len(array)-1
	for left <= right {
		mid := (left + right) / 2
		if array[mid] == target {
			return mid
		}
		if array[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}

func main() {
	array := []int{1, 5, 35, 112, 258, 324, 456, 512}
	index := BinarySearch(array, 112)
	if index == -1 {
		fmt.Println("Element is not present in array")
	} else {
		fmt.Println("Element is present at index :", index)
	}
}
