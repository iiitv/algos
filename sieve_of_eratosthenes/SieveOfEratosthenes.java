public class SieveOfEratosthenes {

	public static boolean[] sieveOfEratosthenes(int n) {
		int sqrtOfn = (int)Math.sqrt(n) + 1;
		boolean[] primes = new boolean[n + 1];
		for (int i = 2; i < n + 1; ++i) {
			primes[i] = true;
		}
		for (int i = 2; i <= sqrtOfn; ++i) {
			if (primes[i]) {
				for (int j = 2 * i; j < n + 1; j += i) {
					primes[j] = false;
				}
			}
		}
		return primes;
	}

	public static void main(String[] args) {
		int n = 100;
		boolean[] primes = sieveOfEratosthenes(n);
		for (int i = 2; i < n + 1; ++i) {
			if (primes[i]) {
				System.out.print(i + " ");
			}
		}
	}
}