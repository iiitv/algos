import java.util.*;
public class Test {
    public static void main(String args[]) {
        int A[] = new int [1000];
        Random rand = new Random();
        for(int i=0;i<A.length;i++) {
            A[i]=rand.nextInt(200);
        }
        CountingSort bs = new CountingSort(A);
        bs.cSort();
        for(int i=0;i<A.length;i++) {
            System.out.print(A[i]+" ");
        }
    }
}