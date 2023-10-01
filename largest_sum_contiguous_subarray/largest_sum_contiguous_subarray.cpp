//    Kadane Algorithm
//    Largest Sum Contiguous Subarray
//    Time complexity  O(n)

#include<bits/stdc++.h>
using namespace std;

int largestSum_ContiguousSubarray(int arr[], int size){
    int max_sum = INT_MIN;
    int curr_sum = 0;
    for (int i = 0; i < size; i++)            //linear iteration of the array
    {
        curr_sum += arr[i];
        max_sum = max(max_sum, curr_sum);
        if (curr_sum < 0)                   //if current sum is negative, it won't be included...
        {
            curr_sum = 0;
        }
    }
      return max_sum;
} 

int main()
{
    int n = 10;
    int arr[n] = {4, -1, 2, -7, 3, 4, -5, 3, 2, 4};
   
    cout<< "largest sum: "<<largestSum_ContiguousSubarray(arr, n);
    return 0;
}

