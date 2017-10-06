using System;
using System.Collections.Generic;
using System.Linq;

/**
 * Stack implementation using a LinkedList 
 */
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
     * Swaps places between the last and second last element of the stack
     */
    public void Swap()
    {
        if (IsEmpty())
            return;

        T last = stack.Last();

        T secondLast = stack.ElementAt(stack.Count() - 2);

        Pop();
        Pop();

        Push(last);
        Push(secondLast);
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
     * pops and pushes the same element twice
     */
    public  void Duplicate()
    {
        if (IsEmpty())
            return;

        T duplicate = stack.Last();

        Pop();

        Push(duplicate);
        Push(duplicate);
    }

    /**
     * gets the n top elements and rotates them
     * 
     * if left == false then it will move the last element to behind the nth element(from the top)
     * 
     * if left == true it will move the nth element(from the top) last
     */
    public void Rotate(int n, bool left)
    {
        if (n <= 1)
            return;

        if (stack.Count <= 2)
            return;

        n -= 1;

        if(left)
        {
            LinkedListNode<T> node = stack.Last;

            for (int i = 1; i <= n; ++i)
            {
                node = node.Previous;
            }

            T value = node.Next.Value;

            stack.Remove(value);

            Push(value);
        }
        else
        {
            T last = stack.Last();

            Pop();

            LinkedListNode<T> node = stack.Last;

            for(int i = 0; i < n; i++)
            {
                node = node.Previous;
            }

            stack.AddBefore(node.Next, last);
        }
    }
}
