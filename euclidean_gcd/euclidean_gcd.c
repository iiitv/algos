#include<stdio.h>

/*
 * first --> First number
 * second --> Second number
 * There are two implementations: Recursive (euclidean_gcd_recursive) and Non-Recursive (euclidean_gcd)
 */

int euclidean_gcd_recursive(int first, int second) {
	if(second == 0) {
		return first;  // First becomes gcd if second becomes zero
	} else {
		return euclidean_gcd_recursive(second, (first % second));
	}
}

int euclidean_gcd(int first, int second) {
	while(second != 0) {  // Iterate till second becomes zero
		int temp = second;  // Temporary variable to hold value of second which is to be assigned to first later
		second = first % second;
		first = temp;
	}
	return first;  // When second becomes 0, first becomes gcd of both
}

int main() {
	int first = 49;
	int second = 7;
	int answer_recursive = euclidean_gcd_recursive(first, second);
	int answer_iterative = euclidean_gcd(first, second);
	printf("GCD of %d and %d is : %d by recursive algo.\n", first, second, answer_recursive);
	printf("GCD of %d and %d is : %d by iterative algo.\n", first, second, answer_iterative);
	return 0;
}
