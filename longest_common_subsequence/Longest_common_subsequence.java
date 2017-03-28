import java.util.*;

class Function
{
	public int Max_SubArray(int [] a)
	{
		int length = a.length;
		int max_int = 0 , max_till = 0;
		for (int k = 0; k < length; k++) 
		{
			max_int = max_int + a[k];
			if(max_till < max_int)
			{
				max_till = max_int;
			}
			if(max_int < 0)
			{
				max_int = 0;
			}		
		}
		return max_till;
	}
}
class Largest_Sum_SubArray
{
	public static void main(String[] args) 
	{
		Function obj = new Function();
		Random rand = new Random();
		int[] array = new int[100];
		for(int u = 0;u < 100; u++) 
		{
			array[u] = rand.nextInt(100);	
		}
		System.out.println("largest sum subarray: " + obj.Max_SubArray(array));	
	}
}
