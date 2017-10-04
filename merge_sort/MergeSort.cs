/*
Time Complexity: O(n log(n))
Space Complexity: O(n)
*/

using System;

public class MergeSort
{
    /// <summary>
    /// Merges two unsorted halves of an array into one sorted array
    /// first half: from 'first' to 'mid'
    /// second half: from 'mid' to 'last'
    /// </summary>
    /// <param name="a">The original unsorted array</param>
    /// <param name="first">The start index of the first half of the array a</param>
    /// <param name="mid">The middle index of the two halves of the array</param>
    /// <param name="last">The end index of the second half of the array a</param>
    /// <param name="temp">A temporary array for storing the sorted halves</param>
    public static void Merge(int[] a, int first, int mid, int last, int[] temp)
    {
        int currL = first;  //left half pointer
        int currR = mid;    //right half pointer
        int currT;          //current sorted array pointer

        for (currT = first; currT < last; currT++)
        {
            //if left half is element is smaller or right pointer is out of bounds
            if (currL < mid && (currR >= last || a[currL] < a[currR]))
                temp[currT] = a[currL++];
            else
                temp[currT] = a[currR++];
        }

        for (currT = first; currT < last; currT++)
            a[currT] = temp[currT];
    }

    /// <summary>
    /// Recursive method for sorting an array 'a' between two indexes
    /// first and last by using merge sort
    /// </summary>
    /// <param name="a">The original unsorted array</param>
    /// <param name="first">The start index. The array will be sorted starting from this index</param>
    /// <param name="last">The end index. The array will be sorted untill this index</param>
    /// <param name="temp">A temporary array for storing merge results</param>
    public static void DoMergeSort(int[] a, int first, int last, int[] temp)
    {
        if (last - first > 1)
        {
            int mid = first + (last - first) / 2;   //find the middle
            DoMergeSort(a, first, mid, temp);       //sort left half
            DoMergeSort(a, mid, last, temp);        //sort right half
            Merge(a, first, mid, last, temp);       //merge two sorted halves
        }
    }

    /// <summary>
    /// Merge sort helper method. Calls the recursive Merge sort method
    /// </summary>
    /// <param name="a">The original unsorted array</param>
    public static void DoMergeSort(int[] a)
    {
        if (a == null || a.Length <= 1)
            return;
        DoMergeSort(a, 0, a.Length, new int[a.Length]);
    }

    public static void Main()
    {
        int[] a = new int[] {2, 4, 9, 6, 7, 8};
        Console.WriteLine("Before Merge Sort:");
        Console.WriteLine("[{0}]", string.Join(", ", a));
        DoMergeSort(a);
        Console.WriteLine("After Merge Sort:");
        Console.WriteLine("[{0}]", string.Join(", ", a));
    }
}
