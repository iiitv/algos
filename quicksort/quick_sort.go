package main

import "fmt"

// partitionArray finds the pivot index
func partitionArray(data []int, left int, right int) int {
	pivotIndex := left
	for true {
		for data[pivotIndex] <= data[right] && pivotIndex != right {
			right--
		}
		if pivotIndex == right {
			break
		} else if data[pivotIndex] > data[right] {
			data[right], data[pivotIndex] = data[pivotIndex], data[right]
			pivotIndex = right
		}
		for data[pivotIndex] >= data[left] && pivotIndex != left {
			left++
		}
		if pivotIndex == left {
			break
		} else if data[pivotIndex] < data[left] {
			data[left], data[pivotIndex] = data[pivotIndex], data[left]
			pivotIndex = left
		}
	}
	return pivotIndex
}

func quickSort(data []int, begin int, end int) {
	if begin < end {
		pivotIndex := partitionArray(data, begin, end)
		quickSort(data, begin, pivotIndex-1)
		quickSort(data, pivotIndex+1, end)
	}
}

// QuickSort sorts data by quicksort algorithm
// Time complexity : O(n log n)
// Space Complexity : O(n)
func QuickSort(data []int) {
	quickSort(data, 0, len(data)-1)
}

func main() {
	data := []int{1, 1122002, 2, 88171, 6754, 79901, 119856, -312, 1, -2}
	QuickSort(data)
	fmt.Println(data)
}
