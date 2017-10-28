public class BubbleSort {

    private static void sort(int[] list){
        if(list == null || list.length == 0 || list.length == 1)
            return;
        boolean swapped;
        int j = 1;
        do{
            swapped = false;
            for (int i = 0; i < list.length - j; i++) {
                if(list[i] > list[i+1]){
                    int temp = list[i];
                    list[i] = list[i+1];
                    list[i+1] = temp;
                    swapped = true;
                }
            }
            j++;
        }
        while (swapped);
    }

    public static void main(String[] args){
        int[] list = { 8, 4, 6, 1, 10, 7, 2, 5, 9, 3 };
        sort(list);
        for (int a : list) {
            System.out.print(a + " ");
        }
    }
}
