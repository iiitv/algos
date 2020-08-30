/*
 *  Given a rod of length n and an array of prices that contains prices of all pieces of size smaller than n.
 *  Determine the maximum new_prices obtainable by cutting up the rod and selling the pieces.
 *  Time Complexity: O(n^2)
 *  Space Complexity: O(n)
 */

#include <stdio.h>
#include <string.h>

#define max(a, b) (a > b) ? a : b;

int rod_cutting(const int *prices) {
	unsigned int i, j;
	unsigned int n = sizeof(prices);
	int new_prices[n + 1];
	memset(new_prices, 0, n + 1);
	for (i = 1; i < n + 1; ++i) {
		int maxi = -1;
		for (j = 0; j < i; ++j) {
			maxi = max(maxi, (prices[j] + new_prices[i - j - 1]));
		}
		new_prices[i] = maxi;
	}
	return new_prices[n];
}

int main() {
	int prices[] = {10, 52, 84, 93, 101, 17, 117, 20};
	printf("%d\n", rod_cutting(prices));
	return 0;
}
