// radix sort algorithm in c# uploaded by elliot37
using System;
class radix {
    static void Main(string[] args) {
        int[] arr = new int[]{23, 4, 2234, 3253, 46, 43, 1, 23, 45, 67};
        Console.WriteLine("\ngiven array : ");
        foreach (var num in arr) {
            Console.Write(" " + num);
        }

        sorting(arr);
        Console.WriteLine("\nafter sorting : ");
        foreach (var num in arr) {
            Console.Write(" " + num);
        }
        Console.WriteLine("\n");
    }

    static void sorting(int[] arr) {
        int i, j;
        int[] temp = new int[arr.Length];
        for (int k = 31; k > -1; --k) {
            j = 0;
            for (i = 0; i < arr.Length; ++i) {
                bool t = (arr[i] << k) >= 0;
                if (k == 0 ? !t : t)
                    arr[i - j] = arr[i];
                else
                    temp[j++] = arr[i];
            }
            Array.Copy(temp, 0, arr, arr.Length - j, j);
        }
    }
}
