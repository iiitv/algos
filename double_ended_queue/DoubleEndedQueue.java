//package algos.double_ended_queue;

//a java implementation of double ended queue
public class DoubleEndedQueue {
    int front = -1, back = -1;

    public int isempty()// to check whether the queue is empty
    {
        if (front == back && front == -1) {
            return 1;
        }
        if (front > back) {
            front = -1;
            back = -1;
            return 1;
        }
        return 0;

    }

    public int isfull(int n)// to check whether queue is full
    {
        if (front == -1 && back == n - 1)
            return 1;
        return 0;
    }

    public void enque_front(int arr[], int value, int n)// to insert from front
    {
        if (isfull(n) == 1) {
            System.out.println("sorry the queue is full");
            return;
        }
        if (front == 0) {
            System.out.println("cannot enque from front");
            return;
        } else {
            if (back == -1)
                back++;
            if (front == -1) {
                front++;
                arr[front] = value;
            } else
                arr[--front] = value;
            return;
        }
    }

    public void enque_back(int arr[], int value, int n)// to insert from back
    {
        if (isfull(n) == 1) {
            System.out.println("sorry the queue is full");
            return;
        }
        if (back == n - 1) {
            System.out.println("sorry cannot enque from back ");
            return;
        }
        if (isempty() == 1) {
            front++;
            back++;
            arr[back] = value;
            return;
        }

        else {

            back++;
            arr[back] = value;
            return;
        }
    }

    public void deque_front(int arr[])// to delete from front
    {
        if (isempty() == 1) {
            System.out.println("queue is empty");
            return;
        } else {
            System.out.println("the element removed is " + arr[front]);
            front++;
        }
    }

    public void deque_back(int arr[])// to delete from back
    {
        if (isempty() == 1) {
            System.out.println("queue is empty");
            return;
        } else {
            System.out.println("the element removed is " + arr[back]);
            back--;
        }
    }

    public void print(int arr[])// to print the elements in queue
    {
        if (isempty() == 1) {
            System.out.println("queue is empty");
            return;
        }
        for (int i = front; i <= back; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        return;
    }

    public static void main(String args[]) {
        int n;
        n = 100;
        int arr[] = new int[n];

        DoubleEndedQueue obj = new DoubleEndedQueue();// object creation of lab3_q2 file.

        obj.enque_front(arr, 10, n);
        obj.print(arr);
        obj.enque_back(arr, 200, n);
        obj.print(arr);
        obj.enque_front(arr, 11, n);
        obj.print(arr);
        obj.enque_back(arr, 25, n);
        obj.print(arr);

        obj.deque_back(arr);
        obj.print(arr);
        obj.deque_front(arr);
        obj.print(arr);

    }

}
