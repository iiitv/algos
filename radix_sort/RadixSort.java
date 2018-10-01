/**
 * This Java program implements the Radix sort algorithm
 * It's a non-comparative based sorting algorithm, hence its worse case time
 * complexity is O(kn), and space is O(k + n) where k is the bucket size
 */

public class RadixSort {

    private static void radixSort(int[] array) {

        int m = array[0];
        int ex = 1;
        int n = array.length;
        int[] b = new int[10]; // initial bucket

        // loop through the array
        // find the max element
        for(int i = 1; i < n; i++) {
            if(array[i] > m)
                m = array[i];
        }

        while(m / ex > 0) {

            int[] bucket = new int[10];

            for(int i = 0; i < n; i++)
                bucket[(array[i] / ex) % 10]++;
            for(int i = 1; i < 10; i++)
                bucket[i] += bucket[i - 1];
            for(int i = n - 1; i >= 0; i--)
                b[--bucket[(array[i] / ex) % 10]] = array[i];

            for(int i = 0; i < n; i++)
                array[i] = b[i];
            ex *= 10;
        }
    }

    public static void main(String args[]) {
        int test[] = new int[]{170, 45, 75, 90, 802, 24, 2, 6};
        radixSort(test);

        for(int i: test) {
            System.out.print(i + " ");
        }
    }
}
