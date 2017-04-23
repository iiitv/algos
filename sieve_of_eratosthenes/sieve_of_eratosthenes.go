package main

import (
	"fmt"
	"math"
)

// SieveOfEratosthenes returns bool array primes
func SieveOfEratosthenes(n int) []bool {
	primes := make([]bool, n+1)
	sqrtOfN := int(math.Floor(math.Sqrt(float64(n))) + 1)
	for j := range primes {
		primes[j] = true
	}
	for i := 2; i <= sqrtOfN; i++ {
		if primes[i] {
			for j := 2 * i; j < n+1; j += i {
				primes[j] = false
			}
		}
	}
	return primes
}

func main() {
	// Change the value of n to get all primes <= n
	n := 29
	primes := SieveOfEratosthenes(n)
	for i := 2; i <= n; i++ {
		if primes[i] {
			fmt.Println(i)
		}
	}
}
