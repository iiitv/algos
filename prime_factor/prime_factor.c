#include <stdio.h>
#include <string.h>  // for memset
#include <stdbool.h>  // for bool type
#include <math.h>

int prime_factors(int num, int *primes) {
	int cnt = 0;  // index to the last location in the array
	bool flag[num];
	memset(flag, true, sizeof(flag));
	flag[0] = false;
	flag[1] = false;
	for (int i = 2; i*i < num; ++i) {
		if (flag[i]) {
			if (num % i == 0) {
				for (int j = 2 * i; j < num; j += i) {
					flag[j] = false;  // Non prime number; flag is unset
				}
			} else {
				flag[i] = false;  // Not a multiple; flag is unset
			}
		}
	}
	for (int i = 0; i < num; ++i) {
		if (flag[i] && num % i == 0) {
			primes[cnt] = i;
			cnt += 1;
		}
	}
	return cnt;  // returns the size of the prime array
}

int main() {
	int no = 1562;
	int primes[(int)(sqrt(no))];  // array size is sqrt(no)
	int idx = prime_factors(no, primes);
	printf("Prime Factors: ");  // printing of primes
	for (int i = 0; i < idx; i++) {
		printf("%d ", primes[i]);
	}
	printf("\n");
	return 0;
}

