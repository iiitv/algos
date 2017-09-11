using System;

public class EuclideanGCD
{
    public static long euclidean_gcd(long a, long b)
    {
        if(a == 0)
        {
            return (b);
        }
        else
        {
            return euclidean_gcd(b % a, a);
        }
    }

    public static long euclidean_gcd_iterative(long a, long b)
    {
        while (b != 0)
        {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static void Main()
    {
        int a = 9000, b = 145685;
        Console.WriteLine("GCD of " + a + " and " + b + " by recursive is : " + euclidean_gcd(a, b));
        Console.WriteLine("GCD of " + a + " and " + b + " by iterative is : " + euclidean_gcd_iterative(a, b));
        Console.WriteLine("");
    }
}
