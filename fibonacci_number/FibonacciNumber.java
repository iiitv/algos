/*
 *Fibonacci series 1,1,2,3,5,8,13,21...
 *Find the nth value of series.
 */

public class FibonacciNumber {
    
	public static int fibonacciNumber(int n) {
        int sum = 0;
        int b = 0;
        int a = 1;
        if (n == 1) {
        	return 1;
        }
		for (int i = 1;i < n;i++) {
			sum = a + b;
			b = a;
			a = sum;
		}
		return sum;
	}

	public static void main(String[] args) {
        int n = 5;
		System.out.println(fibonacciNumber(n));
	}
}
