package main

import (
        "fmt"
        "math"
)

// N = Limit, change N to check primes till N
const N = 20

// SieveOfEratosthenes Main algorithm, bool type
func SieveOfEratosthenes()[N + 1] bool {
    var primes[N + 1] bool
    sqrtOfn := int(math.Floor(math.Sqrt(N)) + 1)
    for j := range primes {
        primes[j] = true
    }
    for i := 2; i <= sqrtOfn; i++ {
		if primes[i] {
			for j := 2*i; j < N+1; j += i {
				primes[j] = false;
			}
		}
	}
    return primes
}

func main() {
    var primes[N + 1] bool
    primes = SieveOfEratosthenes()
    for i := 2; i <= N; i++ {
        if primes[i] {
            fmt.Println(i)
        }
    }
}
