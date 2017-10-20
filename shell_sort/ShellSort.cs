using System;

public class ShellSort
{
    public static void Main()
    {
        int[] data = new int[] {1000, 45, -45, 121, 47, 45, 65, 121, -1, 103, 45, 34};
        Console.WriteLine("Data to be sorted:");
        Print(data);
        Sort(data);
        Console.WriteLine("Sorted data:");
        Print(data);
    }

    public static void Sort(int[] data)
    {
        for (int i = data.Length / 2; i > 0; i /= 2)
        {
            for (int j = i; j < data.Length; ++j)
            {
                for (int k = j - i; k >= 0; k -= i)
                {
                    if (data[k+i] >= data[k])
                    {
                        break;
                    }
                    else
                    {
                        int temp = data[k];
                        data[k] = data[k+i];
                        data[k+i] = temp;
                    }
                }
            }
        }
    }

    public static void Print(int[] data)
    {
        foreach(int elem in data)
        {
            Console.Write(elem + " ");
        }
        Console.WriteLine("");
    }
}
