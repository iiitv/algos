/*
* first --> First number
* second --> Second number
* There are two implementations:
* Recursive(euclideanGCDRecursive) and Non-Recursive(euclideanGCD)
*/

public class EuclideanGCD {
    static int euclideanGCD(int first, int second) {
        while(second != 0) {        // Iterate till second becomes zero
            int temp = second;      // Temporary variable to hold value of second 
            second = first % second;
            first = temp;
        }
        return first;       // When second becomes 0, first becomes gcd of both
    }


    static int euclideanGCDRecursive(int first, int second) {
        if(second == 0)
            return first;       // First becomes gcd if second becomes zero
        else
            return euclideanGCDRecursive(second, (first % second));
    }


    public static void main(String args[]) {
        int first = 25;
        int second = 5;
        int answer_iterative = EuclideanGCD.euclideanGCD(first, second);
        int answer_recursive = EuclideanGCD.euclideanGCDRecursive(first, second);
        System.out.printf("GCD of %d and %d is : %d by recursive algo.\n", first, second, answer_recursive);
        System.out.printf("GCD of %d and %d is : %d by iterative algo.\n", first, second, answer_iterative);
    }
}
