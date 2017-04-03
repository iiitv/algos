import java.util.Scanner;

public class insertionSort {
	@SuppressWarnings("resource")
	public static void main(String arg[]) {
		insertionSort call = new insertionSort();
		Scanner scan = new Scanner(System.in);
		System.out.println("How many number you want to inter in the array \n");
		int n = scan.nextInt();
		int a[] = new int[n];
		System.out.println("please enter the no. in the array \n");
		for (int i = 0; i < a.length; i++) {
			a[i] = scan.nextInt();
		}
		call.sort(a,n);
		
		for(int i=0; i<a.length; i++){
			System.out.println(a[i]);
		}
	}

	public  void sort(int[] a, int n) {
		 for(int k = 1; k < n; k++){
			int temp = a[k];
			int l = k-1;
			try{
				while( l>=0 && temp < a[l] ){
					a[l+1] = a[l];
					l = l-1;
				}
				a[l+1] = temp;
			}catch(Exception e){
				System.out.println(e);
			}	
		 }
	}
}
