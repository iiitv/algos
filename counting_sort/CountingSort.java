import java.util.Random;

class CountingSort {	//Time complexity = O(n)
    private static void countOccurences(int[] a, int[] c) {	//Basically counting occurences of particular  number and store in its index
        for (int i = 0; i < a.length; i++)	//Counting occurence of each number
            c[a[i]]++;
        for(int i = 1; i < c.length; i++)		//counting total number of numbers less then or equal to that number
            c[i] = c[i-1] + c[i];
    }

    public static int[] countingSort(int[] a, int k) { // For Sorting
        int[] b = new int[a.length];	//b Array stores  sorted array
        int[] c = new int[k+1];		//array  c count occurences
        countOccurences(a, c);
        for (int i = a.length-1; i >= 0; i--) {	//storing number in ascending order in b
            b[c[a[i]]-1] = a[i];	//Stores number to it respective position
            c[a[i]]--;		//Decrease c
        }
        return b;	//Return sorted array
    }

    public static void main(String[] args) {
        int[] A = new int[10000];
        int k = 0;
        Random rand = new Random();
        for (int i = 0; i < A.length; i++) {
            A[i] = rand.nextInt(100);
            if (k < A[i])   //Every number must be between 0 to k
                k = A[i];   //K is max number
        }
        A = countingSort(A, k);
        for (int i = 0; i < A.length; i++)
            System.out.print(A[i] + " ");
    }
}
