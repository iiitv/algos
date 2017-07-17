public class ShellSort {
    /**
    * sorting function
    * Worst case time complexity = O(n^2)
    * Best case complexity = O(nlog(n))
    * n is input size
    */
    public static int[] shellSort(int[] data) {
        for (int i = data.length / 2; i > 0; i /= 2) {
            for (int j = i; j < data.length; ++j) {
                for (int k = j - i; k >= 0; k -= i) {
                    if (data[k + i] >= data[k]) {
                        break;
                    } else {
                        //swap the value
                        int temp = data[k];
                        data[k] = data[k + i];
                        data[k + i] = temp;
                    }
                }
            }
        }
        return data;
    }

    // print function
    public static void print(int[]  data) {
        for (Integer item : data) {
            System.out.println(item);
        }
    }

    public static void main(String[] args) {
        int[]  data = {1000, 45, -45, 121, 47, 45, 65, 121, -1, 103, 45, 34};
        System.out.println("Data to be sorted:");
        print(data);
        System.out.println("Sorted data:");
        data = shellSort(data);
        print(data);
    }
}
