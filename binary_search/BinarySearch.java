public class BinarySearch {

    /**
     * <p>Searches searchElement in arr and returns the index where it's found or -1 if not found.</p>
     *
     * <p>The given array must be already sorted otherwise the results are undefined.</p>
     *
     * <p>If there a duplicate elements, there is no guarantee which one will be found.</p>
     *
     * <p>This implementation avoids a possible overflow while calculating the index for the middle element.
     * @see <a href="https://research.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html">Extra, Extra -
     * Read All About It: Nearly All Binary Searches and Mergesorts are Broken</a></p>
     *
     * @param arr
     * @param searchElement
     * @return
     */
    public static int binarySearch(int[] arr, int searchElement) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2; // identical to (left + right) / 2 but avoids overflow
            if (arr[mid] == searchElement) { // Element found
                return mid;
            }
            if (arr[mid] < searchElement) { // Look in right half
                left = mid + 1;
            } else { // Look in left half
                right = mid - 1;
            }
        }

        return -1;        // Element not found
    }

    public static void main(String[] args) {
        int[] arr = new int[] {1, 5, 35, 112, 258, 324};
        int[] searchArr = new int[] {1, 35, 112, 324, 67};
        int pos;
        for (int i = 0; i < searchArr.length; i++) {
            pos = binarySearch(arr, searchArr[i]);  //search key and get poistion
            if (pos >= 0) {
                System.out.println(searchArr[i] + "-> found at index : " + pos);
            } else {
                System.out.println(searchArr[i] + "-> not found");
            }
        }
    }
}
