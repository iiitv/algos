package main

import "fmt"

// RodCutting computes maximum money that can be earned by cutting a rod of length len(price)
// Time Complexity : O((length^2)
// Space Complexity : O(length)
func RodCutting(price []int) int {
	length := len(price)
	optPrice := make([]int, length+1, length+1)
	for i := 1; i <= length; i++ {
		maxim := -1
		for j := 0; j < i; j++ {
			if maxim < price[j]+optPrice[i-j-1] {
				maxim = price[j] + optPrice[i-j-1]
			}
		}
		optPrice[i] = maxim
	}
	return optPrice[length]
}

func main() {
	price := []int{1, 5, 8, 9, 10, 17, 17, 20, 24, 30}
	fmt.Println(RodCutting(price))
}
