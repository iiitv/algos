using System;

public class EuclideanGCD
{  
    public static int euclidean_gcd(int a, int b)
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
    
    public static void Main()
    {
        int a = 9, b = 15;
        int b1 = euclidean_gcd(a, b);
        Console.Write(b1);
        Console.WriteLine("");
    }
}
