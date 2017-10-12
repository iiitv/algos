
public class RadixSort {

    /**
     * Radix sort algorithm
     * @param array array of elements to be sorted
     */
    static void radixSort(int array[]) {
        int i;
        int m = array[0]; // first element
        int ex = 1;
        int n = array.length;
        int[] b = new int[10]; // first bucket
        // loop through array from
        // second element and compare with m
        for (i = 1; i < n; i++) {
            if (array[i] > m)
                m = array[i];
        }

            while (m / ex > 0) {
            // declare and initialize bucket
            int[] bucket = new int[10];

            for (i = 0; i < n; i++)
                bucket[(array[i] / ex) % 10]++;

            for (i = 1; i < 10; i++)
                bucket[i] += bucket[i - 1];

            for (i = n - 1; i >= 0; i--)
                b[--bucket[(array[i] / ex) % 10]] = array[i];

            for (i = 0; i < n; i++)
                array[i] = b[i];
            ex *= 10;
        }

    }

    public static void main(String args[]) {
        int[] test = new int[]{170, 45, 75, 90, 802, 24, 2, 66};
        radixSort(test);

        System.out.println("Sorted array");
        for(int i: test) {
            System.out.println(i);
        }
    }
}
