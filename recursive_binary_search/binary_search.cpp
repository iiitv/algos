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
    int ar[] = {10,20,50,40,30};
    int ele = 30;    //element to search
    int n = 5;    //size of the array
      
    int result = binarySearch(ar, 0, n-1, ele);
    
    (result == -1) ? cout<<"Element not present in array"<<endl : cout<<"Element present in array at index: "<<result<<endl;
    
    return 0;
 }
