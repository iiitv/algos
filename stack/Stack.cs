using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


class MainClass
{
    public static void Main()
    {
        Stack<string> test = new Stack<string>();

        test.Push("123");
        test.Push("test");
        test.Push("rawr");
        test.Push("Pancake");
        test.Push("Yummy");
        test.Push("321");
        test.Push(":thinking:");

        test.Rotate(3, false);

        test.Peek();

        while (!(test.IsEmpty()))
        {
            test.Pop();
        }
    }
}

class Stack<T>
{
    private LinkedList<T> stack;

    /**
    * Constructs an empty stack
    */
    public Stack()
    {
        stack = new LinkedList<T>();
    }

    /**
    * Adds element at the top of the stack
    */
    public void Push(T data)
    {
        stack.AddLast(data);
    }

    /**
    * Removes the element at the top of the stack
    */
    public void Pop()
    {
        if (IsEmpty())
            return;

        stack.RemoveLast();
    }

    /**
    * Returns true if the stack is empty
    */
    public bool IsEmpty()
    {
        return (!stack.Any());
    }


    /**
    * Returms the last element of the stack
    */
    public T Peek()
    {
        if (IsEmpty())
            return default(T);

        return stack.Last();
    }

    /**
    * gets the n top elements and rotates them
    *
    * if left == false then it will move the last element to behind the nth element(from the top)
    *
    * if left == true it will move the nth element(from the top) to the top
    */
    public void Rotate(int n, bool left)
    {
        if (n <= 1)
            return;

        if (stack.Count < 2)
            return;

        n -= 1;

        if (left)
        {
            LinkedListNode<T> node = stack.Last;

            for (int i = 1; i <= n; ++i)
            {
                node = node.Previous;
            }

            T value = node.Value;

            stack.Remove(value);

            Push(value);
        }
        else
        {
            T last = stack.Last();

            Pop();

            LinkedListNode<T> node = stack.Last;

            for (int i = 0; i < n; i++)
            {
                node = node.Previous;
            }

            stack.AddBefore(node.Next, last);
        }
    }
}

