import java.util.Scanner;

public class BubbleSort {

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the length of array");
        int num = sc.nextInt();
        int[] arr = new int[num];
        
        take_Input(sc,arr);
        display(arr);
        bubble_Sort(arr);
        

    }

    

    
    private static void take_Input(Scanner sc, int[] arr) {
        // TODO Auto-generated method stub
        
        for(int i = 0;i<arr.length;i++) {
            System.out.println("enter element  " + i);
            arr[i] = sc.nextInt();
        }
        
    }
    
    
    
    
    private static void display(int[] arr) {
        // TODO Auto-generated method stub
        
        for(int i = 0;i < arr.length;i++) {
            
            
            System.out.print(arr[i]+"  ");
        }
        
    }
    
    private static void bubble_Sort(int[] arr) {
        // TODO Auto-generated method stub
        
        for(int i = 0;i < arr.length;i++) {
            for(int j = 0;j < arr.length - (i+1);j++) {
                if(arr[j] > arr[j+1])  {
                    swap(arr,j,j+1);
                    
                }
            }
            
        }
        System.out.println("\n\n Sorted array is as follows: \n");
        display(arr);
        
    }




    private static void swap(int[] arr, int i, int j) {
        // TODO Auto-generated method stub
        int temp = 0;
        
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        
        
    }

    
    
    

}
