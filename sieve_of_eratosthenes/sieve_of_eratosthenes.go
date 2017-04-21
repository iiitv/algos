package main

import "fmt"

// N = Limit, change N to check primes till N
const N = 23

// SieveOfEratosthenes : main algorithm function, returns bool type
func SieveOfEratosthenes()[N + 1] bool {
    var primes[N + 1] bool
    for j := range primes {
        primes[j] = true
    }
    for i := 2; i <= N / 2; i++ {
        for j := 2; j <= N / i; j++ {
            primes[i * j] = false
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
