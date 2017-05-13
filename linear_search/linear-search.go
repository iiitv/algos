package main

import "fmt"

func linearSearch(array []int, needle int) int {
	for i, item := range array {
		if item == needle {
			return i
		}
	}
	return -1
}

func main() {
	array := []int{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
	index := linearSearch(array, 10)
	if index == -1 {
		fmt.Println("Number not found")
	} else {
		fmt.Println("10 found at index", index)
	}
}
