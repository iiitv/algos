package main

import "fmt"

// EuclideanGCD finds GCD of given numbers by iterative method
// first : first number
// second : second number
// tmp : temporary variable which hold values
// Time complexity :O(log min(first,second))
func EuclideanGCD(first int, second int) int {
	for second != 0 {
		tmp := second
		second = first % second
		first = tmp
	}
	return first
}

// EuclideanGCDRecursive finds GCD of given numbers by recursion
// first : first number
// second : second number
// Recurrance equation : gcd(first,second) =gcd(second,first mod second),if b!=0 gcd(first,second)=first,if b=0
// Time complexity : O(log min(first,second))
func EuclideanGCDRecursive(first int, second int) int {
	if second != 0 {
		return EuclideanGCDRecursive(second, (first % second))
	}
	return first
}

func main() {
	first := 90
	second := 65
	fmt.Println("GCD of numbers is :")
	fmt.Println(EuclideanGCD(first, second))
	fmt.Println(EuclideanGCDRecursive(first, second))
}
