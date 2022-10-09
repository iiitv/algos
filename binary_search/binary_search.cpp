// C++ program to implement recursive Binary Search
#include <bits/stdc++.h>
using namespace std;
//header file

int binarySearch(int arr[], int low, int high, int target)
{
    if (high >= low){
        int mid = low + (high-low)/2;//middle of the array
        if (arr[mid] == target)
            return mid;//If we find the tarrget element in the middle of the array
        else if(arr[mid] > target)//target element to left of the mid
            return binarySearch(arr, low, mid - 1, target);
        else if(arr[mid] < target)//target element to the right of the mid
            return binarySearch(arr, mid + 1, high, target);
    }
    return -1;//target eleement is not present in the array
}

int main()
{   int n;
    cout<<"Enter the size of array: ";
    cin>>n;
    int *arr= new int[n];
    cout<<"Enter the array(it should be in ascending order)"<<endl;
    for(int i=0;i<n;i++)
        cin>>arr[i];
    int x;
    cout<<"Enter the target element: ";
    cin>>x;
    int result = binarySearch(arr, 0, n - 1, x);
    (result == -1)
        ? cout << "Element is not present in array"
        : cout << "Element is present at index " << result;
    return 0;
}

//Time Complexity: O(log n)
//Space Complexity:O(log n)
