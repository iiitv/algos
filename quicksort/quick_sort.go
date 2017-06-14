package main

import "fmt"

// partitionArray finds the pivot index
func partitionArray(data []int, beg int, end int, pivotIndex int) int {
	left, right := beg, end
	pivotIndex = left
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

// QuickSort sorts data by quicksort algorithm
// Time complexity : O(n log n)
// Space Complexity : O(n)
func QuickSort(data []int, begin int, end int) {
	var pivotIndex int
	if begin < end {
		pivotIndex = partitionArray(data, begin, end, pivotIndex)
		QuickSort(data, begin, pivotIndex-1)
		QuickSort(data, pivotIndex+1, end)
	}
}

func main() {
	data := []int{1, 1122002, 2, 88171, 6754, 79901, 119856, -312, 1, -2}
	QuickSort(data, 0, len(data)-1)
	fmt.Println(data)
}
