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

        Console.WriteLine("Pushing to the stack.");
        int max_size = 10;
        for (int i = 1; i <= max_size; i++)
        {
            string ele = String.Format("{0} duck", i);
            Console.WriteLine("Pushing {0} to the stack", ele);
            test.Push(ele);
        }

        Console.WriteLine("Popping off the stack.");
        for (int i = 1; i <= max_size; i++)
        {
            string ele = test.Pop();
            Console.WriteLine("The stack had '{0}' in it", ele);
        }
        Console.WriteLine("Stack is empty!");
    }
}

class Stack<T>
{
    private LinkedList<T> stack;

    // Constructs an empty stack
    public Stack()
    {
        stack = new LinkedList<T>();
    }

    // Adds element at the top of the stack
    public void Push(T data)
    {
        stack.AddLast(data);
    }

    // Removes the element at the top of the stack
    public T Pop()
    {
        T t = stack.Last();
        stack.RemoveLast();
        return t;
    }
}

