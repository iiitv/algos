// A Stack based C program to find next greater element
// for all array elements.

//Time Complexity : O(n)
//Space Complexity : O(n)

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define stackSize 100

//stack for NGE implementation
struct stackForNGE
{
	int items[stackSize];
	int top;
};

//functions to be used by displayNGE
int pop(struct stackForNGE *p)
{
	int temp;
	if (p->top == -1)
	{
		printf("Error: stack underflow n");
		getchar();
		exit(0);
	}
	else
	{
		int top = p->top;
		temp = p->items[top];
		p->top -= 1;
		return temp;
	}
}

bool isEmpty(struct stackForNGE *p)
{
	return (p->top == -1) ? true : false;
}

void push(struct stackForNGE *p, int x)
{
	if (p->top == stackSize - 1)
	{
		printf("Stack Overflow ! \n");
		getchar();
		exit(0);
	}
	else
	{
		p->top += 1;
		int top = p->top;
		p->items[top] = x;
	}
}

/* dislplays element and NGE pair for all elements of
arr[] of size n */
void displayNGE(int a[], int n)
{
	struct stackForNGE s;
	s.top = -1;
	int element;
	int next;
	int i = 0;
	/* push the first element to stack */
	push(&s, a[0]);

	// iterate for rest of the elements
	for (i = 1; i < n; i++)
	{
		next = a[i];

		if (isEmpty(&s) == false)
		{
			// if stack is not empty, then pop an element from stack
			element = pop(&s);

			/* If the popped element is smaller than next, then
                a) print the pair
                b) keep popping while elements are smaller and
                stack is not empty */
			while (element < next)
			{
				printf("%d --> %d\n", element, next);
				if (isEmpty(&s) == true)
					break;
				element = pop(&s);
			}

			/* If element is greater than next, then push
               the element back */
			if (element > next)
				push(&s, element);
		}

		/* push next to stack so that we can find
           next greater for it */
		push(&s, next);
	}

	/* After iterating over the loop, the remaining
       elements in stack do not have the next greater
       element, so print -1 for them */
	while (isEmpty(&s) == false)
	{
		element = pop(&s);
		next = -1;
		printf("%d --> %d\n", element, next);
	}
}

/* Main Method to test above functions */
int main()
{
	int n;
	printf("Enter the size of the array : ");
	scanf("%d", &n);
	int a[n];
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
	}
	printf("The next Greater element and the Array element pairs : \n");
	displayNGE(a, n);
	return 0;
}
