public class FibonacciNumber {

    // fibonacci function return the nth fibonacci no for all n>0
    public static int fibonacci(int n) {
        if (n == 1 || n == 2) {
            return (n - 1);
        } else {
            // Store second last fibonacci number
            int a = 0;
            // Store last fibonacci number
            int b = 1;
            // Store current fibonacci number which is sum of last and second last fibonacci no
            int fib = 0;
            for (int i = 2; i < n; i++) {
                fib = a + b;
                a = b;
                b = fib;
            }
            return (fib);
        }
    }

    public static void main(String[] args) {
        // n>0
        int n = 5;
        if (n <= 0) {
            System.out.println("n must be greater than 0");
            return;
        }
        System.out.println(fibonacci(n));
    }
}
