//Qs class for implementing queue using two stack with costly dequeue() 
import java.util.Scanner;
class QueueUsingStack {
    int s1[]; //First stack
    int s2[]; //Second stack
    int size; //size of queue
    int topS1; //To maintain top of stack 1
    int topS2; //To maintain top of stack 2
    int count; //To count number of items in queue
    public QueueUsingStack(int s) {
        topS1 = 0;
        topS2 = 0;
        count = 0;
        size = s;
        s1 = new int[size];
        s2 = new int[size];
    }
    public void pushS1(int d) //Function to push an item of stack 1
    {
        s1[topS1] = d;
        topS1++;
    }
    public int popS1() //Function to pop an item of stack 1
    {
        topS1--;
        int temp = s1[topS1];
        return temp;
    }
    public void pushS2(int d) //Function to push an item of stack 2
    {
        s2[topS2] = d;
        topS2++;
    }
    public int popS2() //Function to pop an item of stack 1
    {
        topS2--;
        int temp = s2[topS2];
        return temp;
    }
    public boolean isFull(int c) //Function to check whether queue is full or not
    {
        return (c == size);
    }
    public boolean isEmpty(int c) //Function to check whether queue is empty or not
    {
        return (c == 0);
    }

    public void enqueue(int d) // Function to enqueue an item to the queue
    {
        if (isFull(count)) {
            System.out.println("Queue is full");
            System.exit(0);
        } else {
            pushS1(d);
            count++;
        }
    }
    public int dequeue() //Function to deQueue an item from queue
    {
        int temp, i, dq;
        if (isEmpty(count)) {
            System.out.println("Queue is empty");
            System.exit(0);
        }

        //push all the items in stack 2
        for (i = 0; i < count; i++) {
            temp = popS1();
            pushS2(temp);
        }
        dq = popS2();
        count--;

        //After poping push all the items of stack 2 back into stack 1
        for (i = 0; i < count; i++) {
            temp = popS2();
            pushS1(temp);
        }
        return dq;
    }
    public void display() {
        int i;
        for (i = 0; i < count; i++) {
            System.out.print(s1[i] + " ");
        }
    }
}

//queue_using_stack class with main function to operate QueueUsingStack
public class queue_using_stack {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of Queue");
        int s = sc.nextInt();
        QueueUsingStack obq = new QueueUsingStack(s);
        System.out.println("Enter 1 for Enqueue");
        System.out.println("Enter 2 for Dequeue");
        System.out.println("Enter 3 to display Queue");
        System.out.println("Enter 4 to exit");
        while (true) {
            int ch = sc.nextInt();
            switch (ch) {
                case 1:
                    System.out.println("Enter the number to enqueue");
                    int d = sc.nextInt();
                    obq.enqueue(d);
                    System.out.println("Number enqueued successfully");
                    break;
                case 2:
                    int temp = obq.dequeue();
                    System.out.println(temp + " is dequeued");
                    break;
                case 3:
                    obq.display();
                    break;
                case 4:
                    System.exit(0);
            }
        }
    }
}



/*Output:


Enter 1 for implementing Queue using Stack
Enter 2 for implementing Stack using Queue
1
Enter the size of Queue
3
Enter 1 for Enqueue
Enter 2 for Dequeue
Enter 3 to display Queue
Enter 4 to exit
1
Enter the number to enqueue
1
Number enqueued successfully
1
Enter the number to enqueue
2
Number enqueued successfully
1
Enter the number to enqueue
3
Number enqueued successfully
2
1 is dequeued
3
2 3 
*/
