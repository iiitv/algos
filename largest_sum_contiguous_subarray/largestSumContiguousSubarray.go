package main

import "fmt"

// largestSumContinousSubArray is main kadane's algorithm function
func largestSumContinousSubArray(arr []int) int {
	maxTill := 0
	maxTemp := 0
	size := len(arr)
	for i := 0; i < size; i++ {
		maxTemp = maxTemp + arr[i]
		if maxTill < maxTemp {
			maxTill = maxTemp
		}
		if maxTemp < 0 {
			maxTemp = 0
		}
	}
	return maxTill
}

func main() {
	array := []int{-2, -3, 3, -1, -2, 1, 5, -3}
	fmt.Println(largestSumContinousSubArray(array))
}
