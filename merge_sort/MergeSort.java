public class MergeSort {

    private static void merge(int[] a, int first, int mid, int last) {
        int l = mid - first + 1;
        int r = last - mid;
        int[] left = new int[l];
        int[] right = new int[r];

        for (int i = 0; i < l; i++) {  //copy left
            left[i] = a[first + i];
        }
        for (int j = 0; j < r; j++) {  //copy right
            right[j] = a[mid + j + 1];
        }
        int i = 0;
        int j = 0;
        int k = first;
        while (i < l && j < r) {  //merging
            if (left[i] <= right[j]) {
                a[k] = left[i];
                i++;
            } else {
                a[k] = right[j];
                j++;
            }
            k++;
        }
        while (i < l) {  //remainig left element
            a[k] = left[i];
            i++;
            k++;
        }
        while (j < r) {  //remainig right element
            a[k] = right[j];
            j++;
            k++;
        }
    }

    private static void mergeSort(int[] a, int first, int last) {
        if (first < last) {
            int mid = (first + last) / 2;  //find the middle
            mergeSort(a, first, mid);  //sort left half
            mergeSort(a, mid + 1, last);  //sort right half
            merge(a, first, mid, last);  //merge above two sorted halves
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[] {2, 4, 9, 6, 7, 8};
        mergeSort(arr, 0, arr.length - 1);
        for (int element : arr) {
            System.out.println(element);
        }
    }
}
