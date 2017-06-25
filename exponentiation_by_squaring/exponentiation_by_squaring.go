package main

import "fmt"

// ExponentiationBySquaring calculates base^power efficiently.
func ExponentiationBySquaring(base int, power int) int {
	if power < 0 { // Negative power case
		return ExponentiationBySquaring((1 / base), -power)
	} else if power == 0 { // Base case1
		return 1
	} else if power == 1 { // Base case2
		return base
	} else if power%2 == 0 {
		return ExponentiationBySquaring(base*base, power/2)
	} else {
		return base * ExponentiationBySquaring(base*base, (power-1)/2)
	}
}

func main() {
	base, power := 5, 10
	fmt.Println(ExponentiationBySquaring(base, power))
}
