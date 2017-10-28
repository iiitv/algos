public class BubbleSort {

    private static void sort(int[] list) {
        // if the list is null or has zero/one element, we are ready
        if (list == null || list.length == 0 || list.length == 1) {
            return;
        }
        boolean swapped;
        int j = 1;
        // for every iteration, go through the whole list and check if it is sorted
        do {
            swapped = false;
            // for every iteration we know for sure, that the last number ist sorted, so we can ignore them (j)
            for (int i = 0; i < list.length - j; i++) {
                // if the numbers are not sorted, swap them and set swapped to true, to go through the list again.
                if (list[i] > list[i+1]) {
                    int temp = list[i];
                    list[i] = list[i+1];
                    list[i+1] = temp;
                    swapped = true;
                }
            }
            j++;
        } while (swapped);
    }

    public static void main(String[] args) {
        int[] list = {8, 4, 6, 1, 10, 7, 2, 5, 9, 3};
        sort(list);
        for (int a : list) {
            System.out.print(a + " ");
        }
    }
}
