import java.util.ArrayList;

public class PrimeFactor {

    public static ArrayList<Integer> primeFactor(int n) {
        ArrayList<Integer> primeNo = new ArrayList<Integer>();
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                primeNo.add(i);
                while (n % i == 0) {
                    n = n / i;
                }
            }
        }
        return primeNo;
    }

    public static void main(String[] args) {
        int n = 8;
        System.out.println("Prime Factors are:");
        for (Integer i : primeFactor(n)) {
            System.out.println(i);
        }
    }
}
