/**
 *
 * @author jsroyal
 */
public class BinarySearch {

    public static void main(String[] args) {
        int arr[] = {1, 5, 35, 112, 258, 324},
                search_arr[] = {1, 35, 112, 324, 67},
                pos, i;
        BinarySearch obj = new BinarySearch();

        for (i = 0; i < 5; i++) {
            pos = obj.binary_search(arr, 6, search_arr[i]);

            if (pos >= 0) {
                System.out.println(search_arr[i] + "-> found at index : " + pos);
            } else {
                System.out.println(search_arr[i] + " -> not found");
            }
        }

    }

    public int binary_search(int arr[], int arr_size, int search_element) {
        int left = 0, right = arr_size - 1;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] == search_element) // Element found
            {
                return mid;
            }
            if (arr[mid] < search_element) // Look in right half
            {
                left = mid + 1;
            } else // Look in left half
            {
                right = mid - 1;
            }
        }

        return -1;				// Element not found
    }

}
