
public class BinarySearch {

    public static void main(String[] args) {
        int[] arr = {1, 5, 35, 112, 258, 324},
                searchArr = {1, 35, 112, 324, 67};
        int pos;
        for (int i = 0; i < 5; i++) {
            pos = binarySearch(arr, 6, searchArr[i]);
            if (pos >= 0) {
                System.out.println(searchArr[i] + "-> found at index : " + pos);
            } else {
                System.out.println(searchArr[i] + " -> not found");
            }
        }

    }

    static int binarySearch(int[] arr, int arrSize, int searchElement) {
        int left = 0, right = arrSize - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] == searchElement) // Element found
            {
                return mid;
            }
            if (arr[mid] < searchElement) // Look in right half
            {
                left = mid + 1;
            } else // Look in left half
            {
                right = mid - 1;
            }
        }

        return -1;              // Element not found
    }

}
