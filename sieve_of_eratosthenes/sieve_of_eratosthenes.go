package main

import "fmt"

const N = 23

func SieveOfEratosthenes()[N + 1] bool {
    var primes[N + 1] bool
    var i int
    for j := range primes {
        primes[j] = true
    }
    for i = 2; i <= N / 2; i++ {
        for j := 2; j <= N / i; j++ {
            primes[i * j] = false
        }
    }
    return primes
}

func main() {
    var primes[N + 1] bool = SieveOfEratosthenes()
    for i := 2; i <= N; i++{
        if primes[i] {
            fmt.Println(i)
        }
    }
}
