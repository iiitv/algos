import java.util.Random;
 class CountingSort {
	
	public static void main(String[] args) {
		
		int A[]=new int[10000];
        int k=0;
        Random rand=new Random();
        for(int i=0;i<A.length;i++) {
            A[i]=rand.nextInt(100);
            if(k<A[i])
            	k=A[i];
            }
        
        A=cSort(A,k);
        for(int i=0;i<A.length;i++)
        	System.out.print(A[i] + " ");
	}

	public static int[] cSort(int[] a,int k) {
		int[] b=new int[a.length];
		int[] c= new int[k+1];
		 getC(a,c);
        for(int i=a.length-1;i>=0;i--){
            b[c[a[i]]-1]=a[i];
            c[a[i]]--;
        }
            
        return b;	
	}
	private static void getC(int[] a, int[] c) {
       for(int i=0;i<a.length;i++)
           c[a[i]]++;
       for(int i=1;i<c.length;i++)
           c[i]=c[i-1]+c[i];
    }

}