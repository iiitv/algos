/*
Problem Statement: Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Time Complexity: O(n^2)
Space Complexity: O(n)
*/

public class RodCutting {

    public static int cutRod(int[] price) {
        int n = price.length;
        int[] best_price = new int[n+1];
        best_price[0] = 0;
        for (int i = 1; i <= n; i++) {
            int tmax = Integer.MIN_VALUE;
            for (int j = 0; j < i; j++)
                tmax = Math.max(tmax, price[j] + best_price[i-j-1]);
            best_price[i] = tmax;
        }
        return best_price[n];
    }

    public static void main(String[] args) {
        int[] price = new int[] {10, 52, 84, 93, 101, 17, 117, 20};
        System.out.println("Maximum Obtainable Value is " + cutRod(price));
    }
}
