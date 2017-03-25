public class QuickSort {

    private static int partition(int[] a, int l, int r) {
        int pivot = a[r];
        while (l < r) {
            while (a[l] < pivot) { //from left move
                l++;               
            }
            while (a[r] > pivot) {  //from right move
                r--;
            }
            if (l <= r) {
                int temp = a[l];        
                a[l] = a[r];
                a[r] = temp;
            }
        }
        return l; //pivot index
    }

    public static void quickSort(int[] a, int left, int right) {
        if (left < right) {
            int pi = partition(a, left, right);  //pi index of pivot
            quickSort(a, left, pi-1);  //sort left of pivot
            quickSort(a, pi, right);  //sort right of pivot               
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[] {2, 4, 9, 6, 7, 8};
        quickSort(arr, 0, arr.length - 1);
        for (int element : arr) {
            System.out.println(element);
        }
    }
}
