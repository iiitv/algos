public class BinarySearch {

    private static int binarySearch(int[] arr, int searchElement) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
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
