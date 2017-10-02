/*Linear Search algorithm searches for a given number in array
Time complexity is O(n) , n is size of array*/

using System;

public class LinearSearch
{
    public static int Search(int[] data, int target)
    {
        for (int i = 0; i < data.Length; i++)
            if (data[i] == target)
                return i;
        return -1;
    }

    public static void Main()
    {
        int[] array = new int[100];
        // Initializing array with 1,2,....,100
        for(int i = 1; i <= 100; i++)
            array[i-1] = i;
        // Elements to be searched in the array
        int[] search = {12,55,34,102,78};
        for(int i = 0; i < 5; i++)
        {
            int index = Search(array, search[i]);
            if(index >= 0)
                Console.WriteLine(search[i] + " found at index " + index);
            else
                Console.WriteLine(search[i] + " not found in the list");
        }
    }
}
