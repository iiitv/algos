/*
   *   Implementation of famous dynamic programming problem
   *   Largest Sum Contiguous Subarray
   *   Kadane Algorithm 
   *   Time complexity  O(n)
*/
import java.io.PrintWriter;
class largest_sum_contiguous_subarray{
	 static int maxSubarraySum(int[] array){   //  maximum sum method implemention
		int prevSum,currentSum,i;
		prevSum=array[0];					// initialize current sum amd previous sum
		currentSum=array[0];			 	
		for(i=1;i<array.length;i++){
			currentSum += array[i];				// add values in current sum
			if(currentSum<0){				// if current sum is negative , make it zero
				currentSum=0;
			}else{
				if (currentSum > prevSum) {		// if current sum is greate than previous sum
					prevSum=currentSum;		// update previous sum
				}
			}
		}
		return prevSum;
	}
	public static void main(String ar[]){
			PrintWriter pr = new PrintWriter(System.out, true);
			int[] array = {1,3,-7,1,1};     
			int maxSum=maxSubarraySum(array);  /// call method
			pr.print("Maximum SubArray Sum:"+"\t");
			pr.println(maxSum);                     // print output
	}
}



