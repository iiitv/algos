int LinearSearch(List<int> a, number) {
  for (int i = 0; i < a.length; i++) {
    if (a[i] == number) {
      return i;
    }
  }
  return -1;
}

void main() {
  List<int> list = [10,20,30,40,50,60,70,80,90,100];
  int x = 30;
  int index = LinearSearch(list, x);
  
  if (index != -1) {
    print('$x found at positions: $index');
  } else {
    print('$x Not found');
  }
}