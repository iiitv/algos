using System;

public class CountingSort
{

    /**
    * Sorts the array using counting sort
    * Time Complexity: O(n + k) where n is the number of elements in the array and k is the range of input
    * Space Complexity: O(n + k)
    */
    public static int[] DoCountingSort(int[] arr)
    {
        // finding the maximum value in the array
        int maxValue = Int32.MinValue;
        foreach (int num in arr)
            maxValue = Math.Max(maxValue, num);

        // counting the frequency of each element in the array
        int[] frequency = new int[maxValue + 1];
        foreach (int num in arr)
            frequency[num]++;

        // modifying each element in the frequency array to the total of all the elements before it
        for (int i = 1; i < frequency.Length; i++)
            frequency[i] += frequency[i - 1];

        // constructing the sorted array based on the freqency of each element in ascending order
        int[] sortedArr = new int[arr.Length];
        for (int i = 0; i < arr.Length; i++) {
            sortedArr[frequency[arr[i]] - 1] = arr[i];
            frequency[arr[i]]--;
        }
        return sortedArr;
    }

    public static void Main()
    {
        int[] arr = new int[] {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
        int[] sortedArr = DoCountingSort(arr);
        foreach (int num in sortedArr)
            Console.WriteLine(num);
    }
}
