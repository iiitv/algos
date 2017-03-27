/*
 *   Implementation of famous dynamic programming problem
 *   Largest Sum Contiguous Subarray
 *   Kadane Algorithm
 *   Time complexity  O(n)
 */
#include <iostream>
using namespace std;

int largestSumContiguousSubarray(int length, int arr[]) {
    int prevSum;
    int currentSum;
    int i;
    prevSum = arr[0];						    // initialize current sum and previous sum
    currentSum = arr[0];
    for (i = 1; i < length; i++) {
        currentSum += arr[i];				        // add values in current sum
        if (currentSum < 0) {					   // if current sum is negative , make it zero
            currentSum = 0;
        }
        else if (currentSum > prevSum) {           // if current sum is great than previous sum
            prevSum = currentSum;                  // update previous sum
        }
    }
    return prevSum;
}

int main() {
    int arr[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int length = sizeof(arr)/sizeof(arr[0]);         // Length(Size) of the array
    cout << "Largest Sum of Contiguous Subarray = " << largestSumContiguousSubarray(length, arr) << "\n";
    return 0;
}
