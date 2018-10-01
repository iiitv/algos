import java.util.Arrays;

/**
 * <p>This class represents a Sieve of Eratosthenes. It exposes an isPrime(int) method.</p>
 *
 * <p>When creating a Sieve, you need to specify the max number that you might query.</p>
 *
 * <p>Time complexity for creating the Sieve is O(n * n) but for querying is O(1). Space complexity is O(n)</p>
 *
 * @see <a href="https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes">Sieve of Eratosthenes</a>
 */
public class SieveOfEratosthenes {

    private boolean[] sieve;

    /**
     * Creates a sieve that can be queried for numbers up to maxNumber.
     *
     * @param maxNumber
     */
    public SieveOfEratosthenes(final int maxNumber) {
        initSieve(maxNumber);
        crossMultiplesOfKnownPrimes();
    }

    private void initSieve(int maxNumber) {
        this.sieve = new boolean[maxNumber + 1];
        Arrays.fill(sieve, true);
        cross(0);
        cross(1);
    }

    /**
     * Iterates the sieve and when it finds a prime in it, it'll cross its multiples, since by definition those numbers are not prime.
     */
    private void crossMultiplesOfKnownPrimes() {
        for (int n = 2; n * n < sieve.length; ++n) {
            if (isPrime(n)) {
                crossMultiplesOf(n);
            }
        }
    }

    /**
     * Given prime, crosses all multiples of prime in the sieve
     *
     * @param prime
     */
    private void crossMultiplesOf(final int prime) {
        for (int n = prime * prime; n < sieve.length; n += prime) {
            cross(n);
        }
    }

    /**
     * Marks n as a non-prime in the sieve.
     *
     * @param n
     */
    private void cross(final int n) {
        sieve[n] = false;
    }

    /**
     * Returns true if n is a prime number, false otherwise.
     *
     * @param n
     * @return
     */
    public boolean isPrime(final int n) {
        return sieve[n];
    }

    public static void main(String[] args) {
        int max = 100;
        SieveOfEratosthenes sieve = new SieveOfEratosthenes(max);
        for (int n = 0; n < 100; ++n) {
            if (sieve.isPrime(n)) {
                System.out.println(n);
            }
        }
    }
}
