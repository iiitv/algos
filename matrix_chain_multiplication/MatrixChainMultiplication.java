public class MatrixChainMultiplication {	
	
	// Recursive Solution: Exponential Time Complexity
	
	public static int recursive(int a[], int i, int j) 
	{
		// Base Case
		if(i>=j)
			return 0;
		
		int min = Integer.MAX_VALUE;		
		for(int k=i;k<=j-1;k++) 
		{
			// recursive call to fetch the cost
			int tempans = recursive(a, i, k) + recursive(a, k+1, j) + a[i-1]*a[k]*a[j];
			if(tempans<min)
				min=tempans;
		}
		return min;
	}
	

	
	
	// Memoized Recursive Solution (Bottom-Up): O(n^3) time complexity and O(n^2) auxilliary space
	
	public static int memo[][] = new int [1001][1001];  // 2-D memo array to store subproblems
	public static int memoized(int a[], int i, int j) 
	{
		// Base Case
		if(i>=j)
			return 0;
		
		// Checking if solution to subproblem exists
		if(memo[i][j]!=0)
			return memo[i][j];
		
		
		memo[i][j] = Integer.MAX_VALUE;
		for(int k=i;k<=j-1;k++) 
		{
			// memoization of the optimal cost for subproblems
			memo[i][j] = Math.min(memo[i][j], memoized(a, i, k)+memoized(a, k+1, j)+a[i-1]*a[k]*a[j]);
		}
		return memo[i][j];
	}
	
	
	
	
	// Solution by Tabulation (Top-down): O(n^3) time complexity and O(n^2) auxilliary space
	
	public static int tabulated(int a[], int n) 
	{
		int dp[][] = new int[n][n];  // dp of size nxn to store solutions of subproblems
		
		// L is the length of the Matrix chain (Minimum L = 2)
		for(int L = 2; L < n; L++) 
		{
			for(int i = 1; i < n-L+1; i++) 
			{
				int j = i+L-1;
				if(j==n)
					continue;
				
				dp[i][j] = Integer.MAX_VALUE;
				
				for(int k = i; k <= j-1; k++) 
				{
					// dp[i][j] = Minimum number of scalar multiplications needed to compute the sub-matrix
					dp[i][j] = Math.min(dp[i][j], dp[i][k]+dp[k+1][j]+a[i-1]*a[k]*a[j]);
				}
			}
		}
		return dp[1][n-1];	
	}
	
	
	
	
	// Driver Function
	
	public static void main(String args[]) {
		
		int a[] = {2,3,1,4,3}; // Array containing n elements comprising of dimensions of n-1 matrices
		int n = a.length;
		// In the above array, Matrix M1:2x3, M2:3x1, M3:1x4, M4:4x3
		
		System.out.println("Answer by Recursive Approach: "+recursive(a,1,n-1));
		System.out.println("Answer by Memoized Recursive Solution (bottom-up): "+memoized(a,1,n-1));
		System.out.println("Answer by Tabulation (top-down): "+tabulated(a, n));
	}
}
