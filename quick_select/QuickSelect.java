public class QuickSelect {
    /*
     * partition function
     * array     : array on which partitioning has to be done
     * left      : left index of the partitioning subarray
     * right     : right index of the partitioning subarray
     * pivotIndex : pivot index from which partition has to done
     * return    : the index of the last element of the left subarray
     */
    private static int partition(int[] array, int left, int right, int pivotIndex) {
        int pivotValue = array[pivotIndex];
        int temp = array[right];
        array[right] = array[pivotIndex];
        array[pivotIndex] = temp;
        int storeIndex = left;
        while (left < right) {
            if (array[left] < pivotValue) {
                temp = array[storeIndex];
                array[storeIndex] = array[left];
                array[left] = temp;
                storeIndex++;
            }
            left++;
        }
        temp = array[right];
        array[right] = array[storeIndex];
        array[storeIndex] = temp;
        return storeIndex;
    }

    /*
     * Quick Select function
     * left        : left index of the subarray
     * right       : right index of the subarray
     * pos         : position to find the element using quick sort
     * return      : the value of element at pos place in the sorted array
     */
    public static int quickSelect(int[] array, int left, int right, int pos) {
        int pivotIndex;
        if(pos < 0 || pos >= array.length) {
            throw new IndexOutOfBoundsException("index: " + pos);
        }
        if (left == right) {
            return array[left];
        }
        pivotIndex = right - 1;
        pivotIndex = partition(array, left, right, pivotIndex);
        if (pos == pivotIndex) {
            return array[pivotIndex];
        }
        else if (pos < pivotIndex) {
            return quickSelect(array, left, pivotIndex - 1, pos);
        }
        else {
            return quickSelect(array, pivotIndex + 1, right, pos);
        }
    }

    public static void main(String[] args) {
        int[] array = {10, 5, 1, 6, 7, 3, 2, 4, 8, 9};
        System.out.println(quickSelect(array, 0, array.length - 1, 3));
    }

}
