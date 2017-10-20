using System;

public class RunLinkedList
{
    public static void Main(string[] args)
    {
        LinkedList<int> list = new LinkedList<int>();

        try
        {
            Console.WriteLine(list.RemoveLast());
        }
        catch (InvalidOperationException)
        {
            Console.WriteLine("The list is empty");
        }

        list.Add(2, 0);
        Console.WriteLine(list); // [2]

        list.Remove(0);
        Console.WriteLine(list); // Empty

        list.AddFront(2);
        list.Add(5, 1);
        list.Add(10, 2);
        list.AddLast(3);
        Console.WriteLine(list); // [2, 5, 10, 3]

        Console.WriteLine(list.Search(5)); // 1
        Console.WriteLine(list.Search(0)); // -1

        list.RemoveLast();
        Console.WriteLine(list); // [2, 5, 10]

        list.RemoveFront();
        Console.WriteLine(list); // [5, 10]

        Console.WriteLine(list.IsEmpty()); // False

        while (!list.IsEmpty())
        {
            list.RemoveLast();
        }

        Console.WriteLine(list.IsEmpty()); // True

        Console.ReadKey();
    }
}

public class LinkedList<T>
{
    public class Node<U>
    {
        public U data;
        public Node<U> next;

        public Node(U obj)
        {
            this.data = obj;
            this.next = null;
        }
    }

    private Node<T> head;
    public int size = 0;

    public LinkedList()
    {
        this.head = null;
    }

    public void AddFront(T obj)
    {
        Node<T> node = new Node<T>(obj);
        node.next = this.head;
        this.head = node;
        this.size++;
    }

    public void AddLast(T obj)
    {
        if (this.head == null)
        {
            Node<T> node = new Node<T>(obj);
            this.head = node;
            this.size = 1;
        }
        else
        {
            Node<T> temp = this.head;
            while (temp.next != null)
            {
                temp = temp.next;
            }
            Node<T> node = new Node<T>(obj);
            temp.next = node;
            size++;
        }
    }

    public void Add(T obj, int index)
    {
        if (index < 0 || index > this.size)
        {
            throw new Exception("Invalid Index");
        }
        Node<T> temp = this.head;
        if (index == 0)
        {
            AddFront(obj);
        }
        else
        {
            for (int i = 0; i < index - 1; i++)
            {
                temp = temp.next;
            }
            Node<T> node = new Node<T>(obj);
            node.next = temp.next;
            temp.next = node;
            this.size++;
        }
    }

    public T RemoveFront()
    {
        if (IsEmpty())
        {
            throw new InvalidOperationException();
        }
        T objRemoved = this.head.data;
        this.head = this.head.next;
        this.size--;
        return objRemoved;
    }

    public T Remove(int index)
    {
        if (IsEmpty())
        {
            throw new InvalidOperationException();
        }
        else if (index < 0 || index > this.size)
        {
            throw new IndexOutOfRangeException("Invalid Index");
        }
        else if (index > 0)
        {
            Node<T> temp = this.head;
            for (int i = 0; i < index - 1; i++)
            {
                temp = temp.next;
            }
            T objRemoved = temp.next.data;
            temp.next = temp.next.next;
            this.size--;
            return objRemoved;
        }
        return RemoveFront();
    }

    public T RemoveLast()
    {
        if (IsEmpty())
        {
            throw new InvalidOperationException();
        }
        T objRemoved;
        if (this.head.next == null)
        {
            objRemoved = this.head.data;
            this.head = null;
        }
        else
        {
            Node<T> temp = this.head;
            while (temp.next.next != null)
            {
                temp = temp.next;
            }
            objRemoved = temp.next.data;
            temp.next = null;
        }
        this.size--;
        return objRemoved;
    }

    public int Search(T obj)
    {
        Node<T> temp = this.head;
        for (int i = 0; i < this.size; i++)
        {
            if (temp.data.Equals(obj))
            {
                return i;
            }
            else
            {
                temp = temp.next;
            }
        }
        return -1;
    }

    public int GetSize()
    {
        return this.size;
    }

    public bool IsEmpty()
    {
        return size == 0;
    }

    public override string ToString()
    {
        string returnString = "";
        Node<T> temp = this.head;
        if (temp != null)
        {
            returnString += "[";
            while (temp != null)
            {
                if (temp.next == null)
                {
                    return returnString += temp.data + "]";
                }
                else
                {
                    returnString += temp.data + ", ";
                    temp = temp.next;
                }
            }
            return returnString;
        }
        return "[]";
    }
}
