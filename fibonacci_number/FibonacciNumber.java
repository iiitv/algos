public class FibonacciNumber {

    public static void fibonacci(int n) {
      if(n == 1) {
        System.out.println("0");
      }
      else if(n == 2) {
        System.out.println("1");
      }
      else {
        int a = 0;     // Store second last fibonacci number
        int b = 1;    // Store last fibonacci number
        int fib = 0;  // Store current fibonacci number which is sum of last and second last fibonacci no
        for(int i = 2; i < n; i++) {
          fib = a + b;
          a = b;
          b = fib;
        }
        System.out.println(fib);
      }
    }

    public static void main(String[] args) {
          int n = 5;           // n>=0
          if(n < 0) {
            System.out.println("n cannot be less than 0");
            return ;
          }
          fibonacci(n);
    }
}
