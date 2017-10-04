using System;

public class MergeSort
{
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
