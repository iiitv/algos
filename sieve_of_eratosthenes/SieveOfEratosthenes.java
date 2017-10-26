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
        uncrossAllNumbers();
        crossObviousNumbers();
        crossMultiplesOfKnownPrimes();
    }

    /**
     * Iterates the sieve and when it finds a prime in it, it'll cross its multiples, since by definition those numbers are not prime.
     */
    private void crossMultiplesOfKnownPrimes() {
        for (int n = 2; nextMultiplePossiblyNotCrossedOf(n) < sieve.length; ++n) {
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
        for (int n = nextMultiplePossiblyNotCrossedOf(prime); n < sieve.length; n = nextMultipleOf(prime, n)) {
            cross(n);
        }
    }

    /**
     * Crosses 0 and 1 which by definition aren't prime.
     */
    private void crossObviousNumbers() {
        cross(0);
        cross(1);
    }

    /**
     * Returns the next multiple of n which is greater than last.
     *
     * @param n
     * @param last
     * @return
     */
    private int nextMultipleOf(final int n, final int last) {
        return n + last;
    }

    /**
     * <p>Returns the next number which is multiple of n, which possibly hasn't been crossed</p>
     *
     * <p>n * 2 has been cross, while crossing the multiples of 2, n * 3 while crossing the multiple of 3, and so on.
     * So the first multiple that possibly hasn't been crossed is n * n.</p>
     *
     * @param n
     * @return
     */
    private int nextMultiplePossiblyNotCrossedOf(final int n) {
        return n * n;
    }

    /**
     * Initializes the sieve to be queried to numbers up to maxNumber.
     *
     * @param maxNumber
     */
    private void initSieve(final int maxNumber) {
        this.sieve = new boolean[maxNumber + 1];
    }

    /**
     * <p>Uncrosses all numbers in the sieve.</p>
     *
     * <p>At the start of the algorithm, all numbers are considered prime, then {@link #crossObviousNumbers()} and
     * {@link #crossMultiplesOfKnownPrimes()} are run to leave only the real primes</p>
     */
    private void uncrossAllNumbers() {
        Arrays.fill(sieve, true);
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
