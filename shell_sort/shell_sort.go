package main

import "fmt"

// ShellSort function returns sorted data
// Worst case time complexity = O(n^2)
// Best case complexity = O(nlog(n))
func ShellSort(data []int) []int {
	for i := len(data) / 2; i > 0; i /= 2 {
		for j := i; j < len(data); j++ {
			for k := j - i; k >= 0; k -= i {
				if data[k+i] >= data[k] {
					break
				} else {
					data[k], data[k+i] = data[k+i], data[k]
				}
			}
		}
	}
	return data
}

func main() {
	data := []int{1000, 45, -45, 121, 47, 45, 65, 121, -1, 103, 45, 34}
	fmt.Println("Data to be sorted: ", data)
	data = ShellSort(data)
	fmt.Println("Sorted data:", data)
}
