package main

import "fmt"

// ModularExponential computes x^y
// Time Complexity : O(log(power))
func ModularExponential(base int64, power int, mod int64) int64 {
	result := int64(1)
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
	base, power, mod := int64(2), 20, int64(100000)
	fmt.Println(ModularExponential(base, power, mod))
}
