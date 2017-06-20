/**
Problem Statement: Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Time Complexity: O(n^2)
Space Complexity: O(n)
 */

public class RodCutting {

    public static int cutRod(int[] price) {
        int n = price.length;
        int[] best_price = new int[n+1];
        for (int i = 1;i < best_price.length;i++)
            best_price[i] = price[i-1];
        for (int i = 1; i <= n; i++)
            for (int j = i; j < n+1; j++)
                best_price[j] = Math.max(best_price[j], best_price[j-i] + best_price[i]);
        return best_price[n];
    }

    public static void main(String[] args) {
        int[] price = new int[] {10, 52, 84, 93, 101, 17, 117, 20};
        System.out.println("Maximum Obtainable Value is " + cutRod(price));
    }
}
