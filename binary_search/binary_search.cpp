/* Program - Binary search over an array
   Author - Harsh Khatore
   Language - C++
   Date - 11.06.2017
*/

#include <iostream>

using namespace std;

/* function to perform binary search
input parameters:
ar - user-input array.
l - left index of array.
r - right index of array.
ele - element to be searched.
*/
int binarySearch(int *ar, int l, int r, int ele)
{
   if (r >= l)
   {
        int mid = l + (r - l)/2;    //calculate mid point of the array
 
        // If the element is present at the middle itself
        // +1 so that it is easier to read
        if (ar[mid] == ele)  return mid+1;   
 
        // If element is smaller than mid, then it can only be present
        // in left subarray
        if (ar[mid] > ele) return binarySearch(ar, l, mid-1, ele);
 
        // Else the element can only be present in right subarray
        return binarySearch(ar, mid+1, r, ele);
   }
 
   // We reach here when element is not present in array
   return -1;
}
 
int main(void)
{
   int n;   //number of elements in array.
   cin >> n;
   
   int *ar = new int[n];    //dynamically allocating array for user-input
   
   for(int i=0;i<n;i++)
       cin>>ar[i];
   
   int ele;   //element to search
   cin >> ele;
   
   int result = binarySearch(ar, 0, n-1, ele);
   
   (result == -1) ? cout<<"Element not present in array"<<endl : cout<<"Element present in array at index: "<<result<<endl;
   
   return 0;
}
