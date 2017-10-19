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

        Console.WriteLine("Pushing to the stack.")
        test.Push("123");
        test.Push("test");
        test.Push("rawr");
        test.Push("Pancake");
        test.Push("Yummy");
        test.Push("321");
        test.Push(":thinking:");

        Console.WriteLine("Popping off the stack.")
        try
        {
            while (true)
            {
                string ele = test.Pop();
                Console.WriteLine("The stack had '{0}' in it", ele);
            }
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine("Stack is empty!");
        }
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
        return stack.RemoveLast();
    }
}