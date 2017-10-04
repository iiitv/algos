using System;
using System.Collections.Generic;

public class QuickSort
{
    /// <summary>
    /// This method returns the index of median of array at i, j, k.
    /// </summary>
    /// <param name="array"> Input array to be sorted.</param>
    /// <param name="i">Left end index of array.</param>
    /// <param name="j">Right end index of array.</param>
    /// <param name="k">Middle index of array.</param>
    /// <returns>Index of median of array at i, j, k</returns>
    private static int Median(IReadOnlyList<int> array, int i, int j, int k)
    {
        if (array[i] > array[j])
        {
            return array[j] > array[k] ? j : k;
        }
        else
        {
            return array[i] > array[k] ? i : k;
        }
    }

    /// <summary>
    /// Perform Partition Operation on array.
    /// Time Complexity: Theta(nLogn)
    /// Auxiliary Space: O(n)
    /// </summary>
    /// <param name="array">Iterable of elements</param>
    /// <param name="start">Pivot value for array</param>
    /// <param name="end">Right limit of array</param>
    /// <returns>return q value for function, used in partitioning of array.</returns>
    private static int Partition(int[] array, int start, int end)
    {
        var index = start - 1;
        var pivotIndex = Median(array, start, end, (start + end) / 2);
        var tmp = array[pivotIndex];
        array[pivotIndex] = array[end];
        array[end] = tmp;
        var pivot = array[end];
        for (var i = start; i < end; ++i)
        {
            if (array[i] > pivot) continue;
            index++;
            tmp = array[i];
            array[i] = array[index];
            array[index] = tmp;
        }
        index++;
        tmp = array[index];
        array[index] = array[end];
        array[end] = tmp;
        return index;
    }

    /// <summary>
    /// Performs sort using partition function.
    /// Time Complexity : O(nlog(n)).
    /// Space Complexity : O(n).
    /// </summary>
    /// <param name="array">Elemens to sort</param>
    /// <param name="left">Left limit of quick sort</param>
    /// <param name="right">Right limit for quick sort</param>
    public static void Quicksort(int[] array, int left, int right)
    {
        if (left >= right) return;
        var pivotIndex = Partition(array, left, right);
        Quicksort(array, left, pivotIndex - 1);
        Quicksort(array, pivotIndex + 1, right);
    }

    public static void Main()
    {
        var arr = new int[] { 1, 2, 1, 2, 3, 1, 2, 2, 1 };
        var right = arr.Length - 1;
        Quicksort(arr, 0, right);
        foreach (var element in arr)
        {
            Console.Write(element + " ");
        }
    }
}