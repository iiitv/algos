#include <bits/stdc++.h> 
using namespace std; 
/* 
	arr->array
	left-> lower index
	right-> upper index
	k-> key(that we want to find in arr)
*/

/*A recursive function to perform binary search and
it return index of searching element in the arr[] if present else return -1*/
int binary_search_recursive(int arr[], int left, int right, int k) 
{ 
	if (right >= left) { 
		int mid = left + (right - left) / 2; 

		// If the element is present at the middle or it may itself 
		if (arr[mid] == k) 
			return mid; 

		// If element is smaller than mid, then we ignore the right subarray 
		if (arr[mid] > k) 
			return binary_search_recursive(arr, left, mid - 1, k); 

		// Else we have to search for element in right subarray 
		return binary_search_recursive(arr, mid + 1, right, k); 
	} 

	// if we reach here, then element was not present 
	return -1; 
} 

// A iterative binary search function 
int binarySearch(int arr[], int left, int right, int k) 
{ 
    while (left <= right) { 
        int mid = left + (right - left) / 2; 
  
        // Check if x is present at mid 
        if (arr[mid] == k) 
            return mid; 
  
        // If x greater, then we ignore left half 
        if (arr[mid] < k) 
            left = mid + 1; 
  
        // If x is smaller, then we ignore right half 
        else
            right = mid - 1; 
    } 
    // if we reach here, then element was not present 
    return -1; 
}

//main method here
int main(void) 
{ 
	int arr[] = { 3, 5, 7, 11, 17 }; 
	int k = 17; //Key
	int n = sizeof(arr) / sizeof(arr[0]); 
	int result = binary_search_recursive(arr, 0, n - 1, k); 
	if(result == -1)
		cout << "recursive::Element is not present in array"<<endl;
	else
		cout << "recursive::Element is present at index " << result<<endl;

	result = binarySearch(arr, 0, n - 1, k); 
    if(result == -1)
    	cout << "iterative::Element is not present in array";
    else
        cout << "iterative::Element is present at index " << result;

	return 0; 
} 
