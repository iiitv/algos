/*
 *   Implementation of famous dynamic programming problem
 *   Largest Sum Contiguous Subarray
 *   Kadane Algorithm
 *   Time complexity  O(n)
 */

public class LargestSumContiguousSubArray {

    public static int largestSumContiguousSubArray(int[] array) {   //  maximum sum method implemention
        int prevSum = array[0];  // initialize current sum amd previous sum
        int currentSum = array[0];
        for (int i = 1; i < array.length; i++) {
            currentSum += array[i];			// add values in current sum
            currentSum = Math.max(currentSum, array[i]); // maximum from current sum and current array value
            prevSum = Math.max(currentSum, prevSum);  // maximum from current sum and previous sum
        }
        return prevSum;
    }

    public static void main(String[] args) {

        int[] array = new int[] {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Largest Sum of Contiguous SubArray:" + "\t" + largestSumContiguousSubArray(array));
    }
}
