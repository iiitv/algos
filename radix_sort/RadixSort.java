package com.gfred;

public class RadixSort {
    public static void radixSort(int array[]) {
        int i;
        int m = array[0];
        int ex = 1;
        int n = array.length;
        int [] b = new int[10]; // initial bucket

        // loop through the array
        //find the max element
        for(i = 1; i < n; i++) {
            if(array[i] > m)
                m = array[i];
        }

        while(m / ex > 0) {
            // initialize bucket
            int[] bucket = new int[10];

            for(i = 0; i < n; i++)
                bucket[(array[i] / ex) % 10]++;
            for(i = 1; i < 10; i++)
                bucket[i] += bucket[i - 1];
            for(i = n - 1; i >= 0; i--)
                b[--bucket[(array[i] / ex) % 10]] = array[i];

            // copy sorted array elements from b into array
            for(i = 0; i < n; i++)
                array[i] = b[i];
            ex *= 10;

        }

    }

    public static void main(String args[]) {
        int test[] = new int[]{170, 45, 75, 90, 802, 24, 2, 66};
        radixSort(test);

        System.out.println("Sorted array:");

        for(int i: test) {
            System.out.println(i + " ");
        }
    }
}
