import java.util.Arrays;
import java.util.Scanner;

/**
 * @author Dipyaman Saha (https://github.com/dipyamansaha) - BUBBLE SORT ALGORITHM -
 *     https://en.wikipedia.org/wiki/Bubble_sort
 */
public class BubbleSortAlgo {
  static void BubbleSort(int[] Arr) {
    int n = Arr.length;

    for (int i = 0; i < (n - 1); i++) {
      int flag = 0;
      for (int j = 0; j < (n - i - 1); j++) {
        if (Arr[j] > Arr[j + 1]) {
          int temp = Arr[j];
          Arr[j] = Arr[j + 1];
          Arr[j + 1] = temp;

          flag = 1;
        }
      }

      if (flag == 0) break;
    }
  }

  public static void main(String[] args) {
    System.out.println("BUBBLE SORT ALGORITHM\n");

    Scanner sc = new Scanner(System.in);

    System.out.print("How many elements do you wanna insert? ");
    int n = sc.nextInt();

    int[] Arr = new int[n];

    System.out.println("Enter the elements: ");
    for (int i = 0; i < n; i++) {
      Arr[i] = sc.nextInt();
    }

    System.out.println("The entered array: " + Arrays.toString(Arr));

    BubbleSort(Arr);
    System.out.println("The sorted array: " + Arrays.toString(Arr));
  }
}
