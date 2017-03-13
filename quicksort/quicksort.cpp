#include<bits/stdc++.h>

using namespace std;

int quickSort(int arr[], int left, int right) {
      int i = left, j = right;
      int tmp;
      int pivot = arr[(left + right) / 2];
 
      /* partition */
      while (i <= j) {
            while (arr[i] < pivot)
                  i++;
            while (arr[j] > pivot)
                  j--;
            if (i <= j) {
                  tmp = arr[i];
                  arr[i] = arr[j];
                  arr[j] = tmp;
                  i++;
                  j--;
            }
      };
      /* recursion */
      if (left < j)
            quickSort(arr, left, j);
      if (i < right)
            quickSort(arr, i, right);

return *arr;
}


int main(){

	int n;	//input array length
	cin >> n;
	
	int A[n];
	for(int i = 0; i<n; i++)	// input array elements
		cin >>  A[i];    
    
    // sorts in ascending order  from index 0 to n-1 index
    quickSort(A,0,n-1);
    
    // verification stdout
    for(int i = 0; i<n; i++)
    	cout << A[i] <<  " ";
   
return 0;
}

