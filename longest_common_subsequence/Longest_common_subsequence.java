import java.util.*;

public class largestCommonSubsequence {
	public static int maxSubArray(int [] a) {
		int maxInt = 0;
		int maxTill = 0;
		for (int k = 0; k < a.length; k++) {
			maxInt = maxInt + a[k];
			if(maxTill < maxInt) {
				maxTill = maxInt;
			}
			if(maxInt < 0) {
				maxInt = 0;
			}		
		}
		return maxTill;
	}
	
	public static void main(String[] args) {
		Random rand = new Random();
		int[] array = new int[100];
		for(int u = 0; u < 100; u++) {
			array[u] = rand.nextInt(100);	
		}
		System.out.println ("largest sum subarray: " + maxSubArray(array));	
	}
}
