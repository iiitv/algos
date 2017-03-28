import java.util.*;
public class Test {
    public static void main(String args[]) {
        double A[] = new double [1000];
        Random rand = new Random();
        for(int i=0;i<A.length;i++) {
            A[i]=rand.nextDouble();
        }
        BinSort bs = new BinSort(A);
        bs.binSort();
        for(int i=0;i<A.length;i++) {
            System.out.print(A[i]+" ");
        }
        
    }
}