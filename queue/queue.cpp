
//@ raunak kumar jaiswal

// function You can use is defined below:
// 1. push()  - to insert a new data in queue
// 2. pop() - to delete a data from a queue
// 3. size() - to get the
// 4. front() -  to get the front data stored in queue
// 5. back() - to get the last stored data in queue
// 6. isEmpty()- to check whether queue is empty or not

#include <iostream>
#include <cstdlib>
using namespace std;
template <class T1, class T2>

class Pair
{
public:
    T1 first;
    T2 second;
    Pair()
    {
    }
    Pair(T1 x, T2 y)
    {
        first = x;
        second = y;
    }
};
template <class T>
class Node
{
public:
    T data;
    Node<T> *next;
    Node(T d)
    {
        data = d;
        next = NULL;
    }
};
template <class T>
class Queue
{
    int sz;
    Node<T> *rear;
    Node<T> *fron;

public:
    Queue()
    {
        fron = rear = NULL;
        sz = 0;
    }

    void push(T item)
    {
        Node<T> *temp = new Node<T>(item);
        ++sz;
        if (rear == NULL)
        {
            rear = temp;
            fron = temp;
            return;
        }
        rear->next = temp;
        rear = temp;
    }

    void pop()
    {
        if (fron == NULL)
            return;

        Node<T> *temp = fron;
        fron = fron->next;

        delete (temp);
        --sz;
        if (fron == NULL)
        {
            sz = 0;
            rear = NULL;
        }
    }
    T front()
    {
        if (fron == NULL)
        {
            exit(0);
        }
        return fron->data;
    }
    int size()
    {
        return sz;
    }
    T back()
    {
        if (rear == NULL)
        {
            exit(0);
        }
        return rear->data;
    }
    bool isEmpty()
    {
        return fron == NULL;
    }
};

int main()
{

    Queue<Pair<Pair<int, string>, int>> qq;

    qq.push({{5, "data"}, 6});
    qq.push({{6, "structure"}, 7});
    qq.push({{7, "fcfs"}, 8});
    qq.push({{8, "queue"}, 9});
    qq.push({{9, "stl"}, 10});
    qq.pop();

    cout << qq.front().first.first << " " << qq.front().first.second << " " << qq.front().second << endl;

    cout << qq.back().first.first << " " << qq.back().first.second << " " << qq.back().second << endl;

    //while loop iterating over all elements and deleting
    cout << "\n--- iterating over all elements -- \n"
         << endl;
    while (!qq.isEmpty())
    {
        cout << qq.front().first.first << " " << qq.front().first.second << " " << qq.front().second << endl;
        qq.pop();
    }
    return 0;
}