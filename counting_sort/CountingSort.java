
package Test;


public class CountingSort {
    //Time Complexity O(n)
    //Constraints NO. must non negative
    int[] a;
    int[] b;
    int[] c;
    public CountingSort(int[] A) {
        a=A;
        int max=a[0];
        for(int i=1;i<a.length;i++) {
            if(a[i]>max)
                max=a[i];
        }
        b=new int[a.length];    
        c=new int[max+1];
    }
    public int[] cSort() {
        getC();
        for(int i=a.length-1;i>=0;i--) {
            b[c[a[i]]-1]=a[i];
            c[a[i]]--;
        }
            
        return b;
}

    private void getC() {
       for(int i=0;i<a.length;i++)
           c[a[i]]++;
       for(int i=1;i<c.length;i++)
           c[i]=c[i-1]+c[i];
    }
    
}

