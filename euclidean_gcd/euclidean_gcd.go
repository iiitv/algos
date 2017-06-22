package main

import "fmt"

// EuclideanGCDIterative finds GCD of given numbers by iterative method
// first : first number
// second : second number
// tmp : temporary variable which hold values
// Time complexity :O(log min(first,second))
func EuclideanGCDIterative(first int, second int) int {
	for second != 0 {
		tmp := first
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
	fmt.Println(EuclideanGCDIterative(first, second))
	fmt.Println(EuclideanGCDRecursive(first, second))
}
