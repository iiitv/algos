#include <iostream>
using namespace std;

void merge(int arr[], int s, int e, int mid) {
    int temp[e - s + 1];
    int i = s;
    int j = mid + 1;
    int k = 0;
    
    // Merge two sorted arrays into a temporary array
    while (i <= mid && j <= e) {
        if (arr[i] <= arr[j]) {
            temp[k] = arr[i];
            k++;
            i++;
        } else {
            temp[k] = arr[j];
            k++;
            j++;
        }
    }
    
    // Copy remaining elements from the first subarray, if any
    while (i <= mid) {
        temp[k] = arr[i];
        k++;
        i++;
    }
    
    // Copy remaining elements from the second subarray, if any
    while (j <= e) {
        temp[k] = arr[j];
        k++;
        j++;
    }
    
    // Copy the merged elements from the temporary array back to the original array
    for (k = 0, i = s; k < e - s + 1; k++, i++) {
        arr[i] = temp[k];
    }
}

void mergesort(int arr[], int s, int e) {
    if (s >= e) {
        return;
    }
    
    // Calculate the middle index
    int mid = s + (e - s) / 2;
    
    // Recursively sort the first and second halves
    mergesort(arr, s, mid);
    mergesort(arr, mid + 1, e);
    
    // Merge the sorted halves
    merge(arr, s, e, mid);
}
int main() {
    int n;
    
    // user input
    cout << "Enter the size of the array: ";
    cin >> n;
    int arr[n];
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Call the merge sort function to sort the array
    mergesort(arr, 0, n - 1);

    // Print the sorted array
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}




