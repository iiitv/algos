int binarySearch(List<int> arr, int userValue, int min, int max) {
  if (max >= min) {
    
    int mid = ((max + min) / 2).floor();
    if (userValue == arr[mid]) {
      return mid;
    } else if (userValue > arr[mid]) {
      binarySearch(arr, userValue, mid + 1, max);
    } else {
      binarySearch(arr, userValue, min, mid - 1);
    }
  }
  return -1;
}

void main() {
  List<int> arr = [0, 1, 3, 4, 5, 8, 9, 22];
  int userValue = 3;
  int min = 0;
  int max = arr.length - 1;
  int index = binarySearch(arr, userValue, min, max);
  
   if (index != -1) {
    print('$x found at positions: $index');
  } else {
    print('$x Not found');
  }
}