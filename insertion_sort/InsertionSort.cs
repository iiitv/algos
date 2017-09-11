using System;

public class InsertionSort
{
    public static void Sort(int[] data)
    {
        int key;
        for(int i = 1; i < data.Length; i++)
        {
            int j  = i - 1;
            key = data[i];
            while (j >= 0 && data[j] > key)
            {
                data[j + 1] = data[j];
                j = j - 1;
            }
            data[j + 1] = key;
        }
    }

    public static void Main()
    {
        int[] arr = new int[] {1000, 45, -45, 121, 47, 45, 65, 121, -1, 103, 45, 34};
        Sort(arr);
        for(int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i] + " ");
        }
        Console.WriteLine("");
    }
}
