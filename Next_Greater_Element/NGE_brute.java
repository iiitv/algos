
import java.util.*;
import java.lang.*;
import java.io.*;

class NGE_brute {
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0)
		{
		    ArrayList<Integer> list = new ArrayList<>();
		    int n=sc.nextInt();
		    int a[]=new int[n];
		    for (int i=0;i<n;i++)
		    {
		        a[i]=sc.nextInt();
		    }
		    
		    for (int i=0;i<n-1;i++)
		    {
		        int flag=0;
		        for(int j=i+1;j<n;j++)
		        {
		            
		            if (a[j]>a[i])
		            {
		                flag=1;
		                list.add(a[j]);
		                break;
		            }
		        }
		        if (flag==0)
		        list.add(-1);
		    }
		    list.add(-1);
		    
		    
		    for (int i=0;i<list.size();i++)
		     {System.out.print(list.get(i)+" ");}
		     System.out.print("\n");
		   
		}
	}
}