public class InsertionSort {

    private static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int j = i - 1;
            int key = arr[i];	// Element to be compared

            /* Move elements of arr[0...i-1], that are
            greater than key, to one position ahead
            of their current position */
            while(j >= 0 && arr[j] > key) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = key;	// Putting key to the position where all numbers before it are sorted
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        insertionSort(arr);

        for (int x: arr) {	// Printing sorted array
            System.out.print(x+" ");
        }
    }
}
