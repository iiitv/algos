#include <stdio.h>
#include <string.h>
#include <math.h>     // for using square root
#include <stdbool.h>  // to include bool datatype

void sieveOfEratosthenes(int n, bool *primes) {
	int i, sqrtOfn = sqrt(n)+1, j;
	memset(primes, true, n+1);
	primes[0] = false;
	primes[1] = false;

	for (i = 2; i <= sqrtOfn; i++) {
		if (primes[i]) {
			for (j = 2*i; j < n+1; j += i) {
				primes[j] = false;
			}
		}
	}
}

int main() {
	int n, k;
	n = 100;
	bool primes[n+1];
	sieveOfEratosthenes(n, primes);
	for (k = 2; k < n; k++) {
		if (primes[k]) {
			printf("%d ", k);
		}
	}
	return 0;
}
