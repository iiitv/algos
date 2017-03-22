public class QuickSort {

    static int partition(int[] a, int first, int last) {
        int pivot = a[last];
        while(first<last) {
            while(a[first] < pivot) {
                first++;               
            }
            while(a[last] > pivot) {
                last--;
            }
            if(first <= last) {
                int temp = a[first];
                a[first] = a[last];
                a[last] = temp;
            }
        }
        return first; //pivot index
    }

    static void quickSort(int[] a, int first, int last) {
        if (first < last) {
            int pi = partition(a,first,last);  //pi index of pivot
            quickSort(a, first, pi-1);  //sort left of pivot
            quickSort(a, pi, last);  //sort right of pivot               
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[]{2, 4, 9, 6, 7, 8};
        quickSort(arr, 0, arr.length - 1);
        for (int element : arr) {
            System.out.println(element);
        }
    }
}
