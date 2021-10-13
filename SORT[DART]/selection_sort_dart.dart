void selectionSort(List list) {
  if (list == null || list.length == 0) return;
  int n = list.length;
  int j, i;
  for (i = 0; i < n; i++) {
    int min = list[i];
    int temp_pos = i;
    for (j = i + 1; j < n; j++) {
      if (min > list[j]) {
        min = list[j];
        temp_pos = j;
      }
    }
        swap(list, i, temp_pos);
  }
}

void swap(List list, int i, int j) {
  int temp = list[i];
  list[i] = list[j];
  list[j] = temp;
}

void main() {
  List l = [14, 2, 17, 1, 9];
  selectionSort(l);
  print(l);
}
