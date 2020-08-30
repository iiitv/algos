import java.io.*;
import java.util.*;

public class NGE_Stack
{
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		while(t-->0)
		{
		    int n = Integer.parseInt(br.readLine());
		    long a[] = new long[n];
		    
		    String s[] = br.readLine().split(" ");
		    
		    for(int i=0;i<n;i++)
		    {
		        a[i] = Long.parseLong(s[i]);
		    }
		   
		   Stack<Long> stack = new Stack<>();
            HashMap<Long,Long> hashmap = new HashMap<>();
            //key = a[i], value= next greater element   

            for(int i=0;i<n;i++)
            {
                while(!stack.isEmpty()&& a[i] > stack.peek() ) hashmap.put(stack.pop() , a[i]) ;
                
                stack.push(a[i]);
            }
	        
	        for(int i=0;i<n;i++)
	        {
	            System.out.print(hashmap.getOrDefault(a[i],(long)-1)+" "); 
	        }
	        System.out.println();
		}
	}
}
	    
	    