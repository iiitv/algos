/*
Time Complexity: Best: O(n log(n)), Average: O(n log(n)), Worst: O(n^2)
Space Complexity: O(log(n))
*/

using System;

public class QuickSort
{

    /// <summary>
    /// Chooses a pivot based on the median of three values in the array (start, mid, end - 1).
    /// Pivot is placed at the beginning of the array.
    /// </summary>
    /// <param name="a">The array</param>
    /// <param name="start">The start pivoting position in the array</param>
    /// <param name="end">The end pivoting position in the array</param>
    public static void ChoosePivot(int[] a, int start, int end)
    {
        int mid = start + (end - start) / 2;
        int median = Math.Max(Math.Min(a[start], a[mid]), Math.Min(Math.Max(a[start], a[mid]), a[end - 1]));
        int pivotPos = Array.IndexOf(a, median);
        Swap(a, pivotPos, start);
    }

    /// <summary>
    /// Partitions an array into two parts based on a pivot.
    /// All values smaller than the pivot will be placed before the pivot in the array.
    /// All values grater than the pivot will be placed after the pivot in the array
    /// </summary>
    /// <param name="a">The array</param>
    /// <param name="start">The start pivoting position in the array</param>
    /// <param name="end">The end pivoting position in the array</param>
    /// <returns>The new position of the pivot in the array</returns>
    public static int Partition(int[] a, int start, int end)
    {
        int pivotPos = start;       //pivot position (index in the array)
        int pivotVal = a[pivotPos]; //the value of the pivot
        int bigStart = start + 1;   //start index of all values greater than the pivot

        for (int curr = start + 1; curr < end; curr++)
        {
            if (a[curr] < pivotVal)
            {
                Swap(a, curr, bigStart);
                bigStart++;
            }
        }

        Swap(a, pivotPos, bigStart - 1);
        pivotPos = bigStart - 1;
        return pivotPos;
    }

    /// <summary>
    /// Sorts an array using the Quick Sort algorithm
    /// </summary>
    /// <param name="a">The array to sort</param>
    /// <param name="start">The start sorting position in the array</param>
    /// <param name="end">The end sorting position in the array</param>
    public static void DoQuickSort(int[] a, int start, int end)
    {
        if(end - start == 2)
        {
            if(a[start] > a[end - 1])
                Swap(a, start, end - 1);
        }
        else if(end - start > 1)
        {
            ChoosePivot(a, start, end);
            int pivotPos = Partition(a, start, end);
            DoQuickSort(a, start, pivotPos);
            DoQuickSort(a, pivotPos + 1, end);
        }
    }

    /// <summary>
    /// Quick Sort helper method
    /// </summary>
    /// <param name="a">The array to sort</param>
    public static void DoQuickSort(int[] a)
    {
        if (a != null && a.Length > 1)
            DoQuickSort(a, 0, a.Length);
    }

    /// <summary>
    /// Swap two index positions in an array
    /// </summary>
    /// <param name="a">The array</param>
    /// <param name="x">The first index</param>
    /// <param name="mid">The second index</param>
    public static void Swap(int[] a, int x, int y)
    {
        int temp = a[x];
        a[x] = a[y];
        a[y] = temp;
    }

    public static void Main()
    {
        int[] arr = new int[] {2, 4, 2, 6, 7, -1};
        DoQuickSort(arr);
        foreach(int element in arr)
        {
            Console.Write(element + " ");
        }
        Console.WriteLine("");
    }
}
