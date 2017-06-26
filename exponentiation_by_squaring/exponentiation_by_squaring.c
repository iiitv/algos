#include<stdio.h>

/* Algorithm to calculate x raised to power k very efficiently
 *  Can be used as a great alternative to normal pow function
 *  base - base of the expression
 *  power - power of expression
 */

long double exponentation_by_squaring(long double base, int power) {
	if (power < 0) {  // Negative power case
		return exponentation_by_squaring(1 / base, -power);
	} else if (power == 0) {  // Base case1
		return 1;
	} else if (power == 1) {  // Base case2
		return base;
	} else if (power % 2 == 0) {
		return exponentation_by_squaring(base * base, power / 2);
	} else if (power % 2 == 1) {
		return base * exponentation_by_squaring(base * base, (power - 1) / 2);
	}
}

int main() {
	long double base = 2;
	int power = 31;
	printf("%LG raised to %d is %LG\n", base, power, exponentation_by_squaring(base, power));

	base = 2;
	power = -2;
	printf("%LG raised to %d is %LG\n", base, power, exponentation_by_squaring(base, power));
	return 0;
}
