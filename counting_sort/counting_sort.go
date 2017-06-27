package main

import "fmt"

// CountingSort sorts the input array in ascending order
// Time complexity is O(z) where z =  max(len(data), max(data))
func CountingSort(data []int) {
	size := len(data)
	temp := make([]int, size)
	max := 0
	for _, elem := range data {
		if elem > max {
			max = elem
		}
	}
	count := make([]int, max+1)
	for _, item := range data {
		count[item]++
	}
	for i := 1; i <= max; i++ {
		count[i] += count[i-1]
	}
	for i := 0; i < size; i++ {
		temp[count[data[i]]-1] = data[i]
		count[data[i]]--
	}
	for i := 0; i < size; i++ {
		data[i] = temp[i]
	}
}

func main() {
	data := []int{1, 202, 2, 675, 901, 116, 312, 1, 2}
	CountingSort(data)
	fmt.Println(data)
}
