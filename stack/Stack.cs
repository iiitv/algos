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
            string ele = String.Format("{0} duck", max_size + 1 - i);
            Console.WriteLine("Pushing {0} to the stack", ele);
            test.Push(ele);
        }

        Console.WriteLine("Currently in the stack: %n {0}", test.ToString());

        Console.WriteLine("Rotating");
        test.Rotate(4, true);
        Console.WriteLine(test.ToString());

        test.Rotate(5, false);
        Console.WriteLine(test.ToString());

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

    public Boolean isEmpty()
    {
        return !stack.Any();
    }

    /*
    * Gets the top n elements and rotates them
    *
    * If left == false then it will move the last element to behind the nth element (from the top)
    *
    * If left == true it will move the nth element(from the top) to the top
    */
    public void Rotate(int n, bool left)
    {
        Stack<T> tmp = new Stack<T>();
        T ele;
        if (left)
        {
            for (int i = 0; i < n; i++)
            {
                tmp.Push(this.Pop());
            }
            ele = tmp.Pop();
        }
        else
        {
            ele = this.Pop();
            for (int i = 0; i < n - 1; i++)
            {
                tmp.Push(this.Pop());
            }
            tmp.Push(ele);
        }
        while(!tmp.isEmpty())
        {
            this.Push(tmp.Pop());
        }
        if(left)
        {
            this.Push(ele);
        }
    }

    public override string ToString()
    {
        Stack<T> tmp = new Stack<T>();
        string s = "Stack: ";
        while (!this.isEmpty())
        {
            T ele = this.Pop();
            s += String.Format("{0} | ", ele.ToString());
            tmp.Push(ele);
        }
        while (!tmp.isEmpty())
        {
            this.Push(tmp.Pop());
        }
        return s;
    }
}

