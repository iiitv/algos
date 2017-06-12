package main

import "fmt"

// InsertionSort function returns sorted data
// Time complexity: O(n^2)
// Space complexity: O(1)
func InsertionSort(data []int) []int {
	for i := 1; i < len(data); i++ {
		key := data[i]
		j := i - 1
		for j >= 0 && data[j] > key {
			data[j+1] = data[j]
			j--
		}
		data[j+1] = key
	}
	return data
}

func main() {
	data := []int{1000, 45, -45, 121, 47, 45, 65, 121, -1, 103, 45, 34}
	data = InsertionSort(data)
	fmt.Println(data)
}
