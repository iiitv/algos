//    Selection Sort

#include <bits/stdc++.h>
using namespace std;

int selectionSort(int arr[], int size)
{
    for (int i = 0; i < size - 1; i++) // We need to n - 2 passes...
    {
        int iMin = i;
        for (int j = i + 1; j < size; j++)
        {
            if (arr[j] < arr[iMin])
            {
                iMin = arr[j]; // Update the index of minimum element
            }
        }
        int temp = arr[i];
        arr[i] = arr[iMin];
        arr[iMin] = temp;
    }
}

int main()
{
    int n = 6;
    int arr[n] = {2, 8, 4, 1, 7, 3};
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}
