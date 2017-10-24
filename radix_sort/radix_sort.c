#include "stdio.h"
#include <time.h>
#include <stdlib.h>

/*
 * Returns maximum number in an array
 * @a array pointer
 * @n number of elements in the array
 */
int max(int * a, int n) {
	int max = a[0];
	for (int i = 1; i < n; i++) {
		if (a[i] > max) {
			max = a[i];
		}
	}
	return max;
}

/*
 * Performs Radix Sort on a given array
 * @a array pointer
 * @n number of elements in the array
 */
void radix_sort(int * a, int n) {
	int m = max(a, n);
	int b[10] = {0};

	for (int exp = 1; m / exp > 0; exp*=10) {
		int bucket[10] = {0};

		for (int i = 0; i < n; i++)
			bucket[(a[i] / exp) % 10]++;
		for (int i = 1; i < n; i++)
			bucket[i] += bucket[i - 1];
		for (int i = n - 1; i >= 0; i--)
			b[--bucket[(a[i] / exp) % 10]] = a[i];

		for (int i = 0; i < n; i++)
			a[i] = b[i];
	}
}

int main() {
	srand(time(NULL));
	int n = 10;

	int test_array[n];
	for (int i = 0; i < n; i++) {
		test_array[i] = rand() % 1000;
	}

	radix_sort(test_array, n);
	for (int i = 0; i < n; i++) {
		printf("%d ", test_array[i]);
	}
	printf("\n");
	return 0;
}
