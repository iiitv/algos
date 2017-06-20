import java.math.BigInteger;

public class ModularExponential {
    public static BigInteger modularExponential(long base, long power, long mod) {
        BigInteger result = BigInteger.ONE;
        base = base % mod;
        while(power > 0) {
            if(power % 2 == 1) {
                result = result.multiply(BigInteger.valueOf(base));
                result = result.mod(BigInteger.valueOf(mod));
            }
            power = power / 2;
            base = (base * base) % mod;
        }
        return result;
    }

    public static void main(String[] args) {
        long base = 78;
        long pow = 20;
        long mod = 65;
        System.out.println(modularExponential(base, pow, mod));
    }
}
