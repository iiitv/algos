/*
 *   Implementation of famous dynamic programming problem
 *   Largest Sum Contiguous Subarray
 *   Kadane Algorithm
 *   Time complexity  O(n)
 */

public class LargestSumContiguousSubarray {

    public static int largestSumContiguousSubarray(int[] array) {   //  maximum sum method implemention
        int prevSum;
        int currentSum;
        int i;
        prevSum = array[0];						// initialize current sum amd previous sum
        currentSum = array[0];
        for (i = 1; i < array.length; i++) {
            currentSum += array[i];				// add values in current sum
            if (currentSum < 0) {					// if current sum is negative , make it zero
                currentSum = 0;
            } else if (currentSum > prevSum) {   // if current sum is greate than previous sum
                prevSum = currentSum;             // update previous sum
            }
        }
        return prevSum;
    }

    public static void main(String[] args) {

        int[] array = new int[] {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Largest Sum of Contiguous Subarray:" + "\t" + largestSumContiguousSubarray(array));
    }
}
