/*
 * Implementation of famous dynamic programming problem
 *  that aims to find out the maximum number of ways in
 *  which a value can be achieved using some fixed valued
 *  coins.
 *
 * In the implementation, the time complexity is O(mn)
 *  and extra space required is O(n).
 */
#include <stdio.h>
#include <string.h>

/*
 * coin: Array containing value of coins
 * m: Number of types of coins
 * n: Value to find the change for
 */
int coin_change_problem(const int *coin, int m, int n) {
	int i, j;
	int possibilities[n+1];

	memset(possibilities, 0, sizeof(possibilities));

	// Base case for n == 0
	possibilities[0] = 1;

	// Build the possibilities table in bottom-up manner
	// For all coins,
	// Update array if the current coin is capable of
	//   incrementing the possibility
	for (i = 0; i < m; i++) {
		for (j = coin[i]; j <= n; j++) {
			possibilities[j] += possibilities[j-coin[i]];
		}
	}

	return possibilities[n];
}

int main() {
	int coin[] = {2, 5, 3, 6};
	int n = 10, m = sizeof(coin)/sizeof(coin[0]);
	printf("%d\n", coin_change_problem(coin, m, n));
	return 0;
}
