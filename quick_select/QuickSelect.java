public class QuickSelect {
    /*
    * partition function
    * array        : array on which partitioning has to be done
    * left      : left index of the partitioning subarray
    * right     : right index of the partitioning subarray
    * pivot_idx : pivot index from which partition has to done
    * store_idx : index of the last element of the left subarray
    * return    : the index of the last element of the left subarray
     */
    public static int partition(int[] array, int left, int right, int pivot_idx) {
        int pivot_value = array[pivot_idx];
        int temp = array[right];
        array[right] = array[pivot_idx];
        array[pivot_idx] = temp;
        int store_idx = left;
        while (left < right){
            if (array[left] < pivot_value){
                temp = array[store_idx];
                array[store_idx] = array[left];
                array[left] = temp;
                store_idx++;
            }
            left++;
        }
        temp = array[right];
        array[right] = array[store_idx];
        array[store_idx] = temp;
        return store_idx;
    }

    /*
    * Quick Select function
    * left        : left index of the subarray
    * right       : right index of the subarray
    * pos         : position to find the element using quick sort
    * pivot_index : pivot index
    * return      : the value of element at pos place in the sorted array
     */
    public static int quickSelect(int[] array, int left, int right, int pos) {
        int pivot_index;
        if (left == right)
            return array[left];
        pivot_index = right - 1;
        pivot_index = partition(array, left, right, pivot_index);
        if (pos == pivot_index)
            return array[pivot_index];
        else if (pos < pivot_index)
            return quickSelect(array, left, pivot_index - 1, pos);
        else 
            return quickSelect(array, pivot_index + 1, right, pos);
    }

    public static void main(String[] args) {
        int array[] = {10, 5, 1, 6, 7, 3, 2, 4, 8, 9};
        System.out.println(quickSelect(array, 0, array.length - 1, 3));
    }

}
