public class QuickSort {

    private static int compare(int[] arr, int i, int j) {
        if (arr[i] > arr[j]) {
            return i;
        } else {
            return j;
        }
    }

    /*
    This method returns the index of median of array at i, j, k.
    @param arr: Input array to be sorted.
    @param i: Left end index of array.
    @param j: Right end index of array.
    @param k: Middle index of array.
    @return: Index of median of array at i, j, k.
    */
    private static int median(int[] arr, int i, int j, int k) {
        if (arr[i] > arr[j] && arr[i] > arr[k]) {
            return compare(arr, k, j);
        } else if (arr[j] > arr[i] && arr[j] > arr[k]) {
            return compare(arr, k, i);
        } else {
            return compare(arr, i, j);
        }
    }

    private static int partition(int[] arr, int start, int end) {
        int l = median(arr, start, end, (start + end) / 2);
        int p_idx = start - 1;
        int tmp = arr[l];
        arr[l] = arr[end];
        arr[end] = tmp;
        int pivot = arr[end];
        for (int i = start; i < end; ++i) {
            if (arr[i] <= pivot) {
                p_idx++;
                tmp = arr[i];
                arr[i] = arr[p_idx];
                arr[p_idx] = tmp;
            }
        }
        p_idx++;
        tmp = arr[p_idx];
        arr[p_idx] = arr[end];
        arr[end] = tmp;
        return p_idx;
    }

    public static void quickSort(int[] a, int left, int right) {
        if (left < right) {
            int pi = partition(a, left, right);  //pi index of pivot
            quickSort(a, left, pi - 1);  //sort left of pivot
            quickSort(a, pi + 1, right);  //sort right of pivot
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[] {2, 4, 2, 6, 7, -1};
        quickSort(arr, 0, arr.length - 1);
        for (int element : arr) {
            System.out.println(element);
        }
    }
}
