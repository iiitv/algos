#include<stdio.h>

/*
* first --> First number
* second --> Second number
*
* There are two implementations: Recursive (gcd_recursive) and Non-Recursive (gcd_iterative)
*
*
*/

int gcd_recursive(int first, int second) {
        if(second == 0)
            return first;      			 //first becomes gcd if second becomes zero
        else
            return gcd_recursive(second, (first % second));
}

int gcd_iterative(int first, int second) {
		while(second ! = 0) {			// Iterate till second becomes zero
			int temp = second;			// temporary variable to hold value of second which is to be assigned to first later
			second = first % second;
			first = temp;
		}

		return first;			// When second becomes 0, first becomes gcd of both
		
}

int main() {
        int first = 49;
        int second = 7;
        int answer = gcd_recursive(first, second);

        printf("GCD of %d and %d is : %d\n",first,second,answer);
}
