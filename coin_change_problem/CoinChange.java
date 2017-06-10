/*
 * Implementation of famous dynamic programming problem
 * that aims to find out the maximum number of ways in
 * which a value can be achieved using some fixed valued
 * coins.
 *
 * In the implementation, the time complexity is O(mn)
 * and extra space required is O(n).
 */
import java.util.Arrays;
/*
 * coin: Array containing value of coins
 * m: Number of types of coins
 * n: Value to find the change for
 */
public class CoinChange {
	static int CoinChangeProblem(int[] C, int m, int n) {
		int[] possibilities = new int[n+1];
		Arrays.fill(possibilities, 0);
		possibilities[0] = 1;
		// Build the possibilities table in bottom-up manner
		// For all coins,
		// Update array if the current coin is capable of
		// incrementing the possibility
		for(int i = 0; i < m; i++){
			for(int j = C[i]; j <= n; j++){
				possibilities[j] += possibilities[j - C[i]];
			}
		}
		return possibilities[n];
	}
	public static void main(String[] args) {
		int[] coin = {2, 5, 3, 6};
		int n = 10, m = coin.length;
		System.out.println(coin_change_problem(coin, m, n));
	}
}
