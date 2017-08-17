package main

import "fmt"

// CoinChangeProblem find out maximum number of ways in which a amount can
// be obtained using fixed value coins.
// Time Complexity :  O((number of type of coins)*amount)
func CoinChangeProblem(coins []int, amount int) int {
	possibilities := make([]int, amount+1)
	possibilities[0] = 1
	for i := 0; i < len(coins); i++ {
		for j := coins[i]; j <= amount; j++ {
			possibilities[j] += possibilities[j-coins[i]]
		}
	}
	return possibilities[amount]
}

func main() {
	coins := []int{1, 2, 3}
	amount := 10
	fmt.Println(CoinChangeProblem(coins, amount))
}
