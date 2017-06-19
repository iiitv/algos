public class QuickSort {

    private static int partition(int[] arr, int start, int end) {
        int pivot = arr[end];
        int p_idx = start - 1;
        int tmp;
        for (int i = start; i < end; ++i) {
            if (arr[i] <= pivot) {
                p_idx++;
                tmp = arr[i];
                arr[i] = arr[p_idx];
                arr[p_idx] = tmp;
            }
        }
        tmp = arr[p_idx + 1];
        arr[p_idx + 1] = arr[end];
        arr[end] = tmp;
        return p_idx + 1;
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
