using System;

public class BinarySearch
{
    public static void Main()
    {
        int[] data = new int[] {1, 5, 6, 8, 13, 45, 65, 121, 123, 163, 245, 334};
        int target = 123;
        int index = Search(data, target);
        if(index >= 0)
        {
            Console.WriteLine("Index of target: " + index);
        }
        else
        {
            Console.WriteLine("Not found\n");
        }
    }

    public static int Search(int[] data, int target)
    {
        int left = 0, right = data.Length;
        while(left <= right)
        {
            int mid = (left + right) / 2;
            if (data[mid] == target)
            {
                return mid;
            }
            if (data[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        return -1;
    }
}
