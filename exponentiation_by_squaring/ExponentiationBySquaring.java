/* Algorithm to calculate base raised to power power very efficiently
*  Can be used as a great alternative to normal pow function
*  base - base of the expression
*  power - power of expression
*/

public class ExponentiationBySquaring {
    public static double exponentiationBySquaring(double base, int power) {
        if (power < 0) {	// Negative powers
            return exponentiationBySquaring(1.0 / base, -power);
        } else if (power == 0) {	// Base case 1
            return 1;
        } else if (power == 1) {	// Base case 2
            return base;
        } else if (power % 2 == 0){	// Even powers
            return exponentiationBySquaring(base * base, power / 2);
        } else {	// Odd powers
            return base * exponentiationBySquaring(base * base, (power - 1) / 2);
        }
    }

    public static void main(String[] args) {
        double base = 2;
        int power = -1;
        System.out.println(base + " raised to " + power + " is: " + exponentiationBySquaring(base, power));
    }
}
