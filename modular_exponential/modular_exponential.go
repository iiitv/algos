package main

import "fmt"

// ModularExponential computes x^y
// Time Complexity : O(log(power))
func ModularExponential(base int, power int, mod int) int {
	result := 1
	base = base % mod
	for power > 0 {
		if power%2 == 1 {
			result = (result * base) % mod
		}
		power = power >> 1
		base = (base * base) % mod
	}
	return result
}

func main() {
	base := 2
	power := 11
	mod := 1000
	fmt.Println(ModularExponential(base, power, mod))
}
