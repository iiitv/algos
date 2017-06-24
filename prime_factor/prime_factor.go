package main

import (
	"fmt"
	"math"
)

// PrimeFactor finds all the prime factor of given number
func PrimeFactor(n int) []int {
	var primes []int
	sqrt := int(math.Sqrt(float64(n)))
	for i := 2; i <= sqrt; i++ {
		if n%i == 0 {
			primes = append(primes, i)
			for n%i == 0 {
				n = n / i
			}
		}
	}
	if n != 1 {
		primes = append(primes, n)
	}
	return primes
}

func main() {
	n := 8
	fmt.Println("Prime Factors are :")
	fmt.Println(PrimeFactor(n))
}
