//QueueUsingStack class for implementing queue using two stack with costly dequeue() 
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
}

//queue_using_stack class with main function to operate QueueUsingStack
public class queue_using_stack {
    public static void main(String args[]) {
        int s = 5;
        QueueUsingStack obq = new QueueUsingStack(s);
        obq.enqueue(1);
        obq.enqueue(2);
        obq.enqueue(3);
        obq.enqueue(4);
        obq.enqueue(5);
        System.out.print(obq.dequeue() + " ");
        System.out.print(obq.dequeue() + " ");
        System.out.print(obq.dequeue() + " ");
        System.out.print(obq.dequeue() + " ");
        System.out.print(obq.dequeue() + " ");
    }
}



/*Output:

1 2 3 4 5
*/
