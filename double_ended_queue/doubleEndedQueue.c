#include <stdlib.h>
#include <stdio.h>

struct Deque
{
	int data;
	struct Deque *next;
};
struct Deque *head = NULL;
struct Deque *last = NULL;

struct Deque *createDeque(struct Deque *root, int key)	//Function to create deque
{
	root = (struct Deque *)malloc(sizeof(struct Deque));
	root->data = key;
	root->next = NULL;
	head = root;
	last = root;
	return head;
}	//O(1) time complexity

struct Deque *push_front(struct Deque *root, int key)	//Function to push element on the front of deque
{
	if (head == NULL)
	{
		return createDeque(root, key);
	}
	struct Deque *temp;
	temp = (struct Deque *)malloc(sizeof(struct Deque));
	temp->data = key;
	temp->next = head;
	head = temp;
	return head;
}	//O(1) time complexity

struct Deque *push_back(struct Deque *root, int key)	//Function to push element to the back of deque
{
	if (head == NULL)
	{
		return createDeque(root, key);
	}
	struct Deque *temp;
	temp = (struct Deque *)malloc(sizeof(struct Deque));
	temp->data = key;
	temp->next = NULL;
	last->next = temp;
	last = temp;
	return last;
}	//O(1) time complexity

struct Deque *pop_front()	//Function to remove or pop the front element
{
	if (head == NULL)
	{
		printf("Deque is empty.\n");
		return head;
	}
	struct Deque *temp;
	temp = head;
	head = head->next;
	free(temp);	//free the unwanted space
	return head;
}	//O(1) time complexity

struct Deque *pop_back()	//Function to remove element from back of deque
{
	if (head == NULL)	//before removing element, checking whether the deque is empty or not
	{
		printf("Deque is empty\n");
		return head;
	}
	struct Deque *temp, *temp2;
	temp = head;
	while (temp->next != last)
	{
		temp = temp->next;
	}
	temp2 = temp->next;
	temp->next = NULL;
	last = temp;
	free(temp2);//free the unwanted space
	return head;
}	//O(n) time complexity

void front()	//Function to give the front element of deque
{
	if (head == NULL)
	{
		printf("Deque is empty.\n\n");
	}
	printf("The element at the front of deque is %d.\n\n", head->data);
}	//O(1) time complexity

void back()	//Function to give the back of deque
{
	if (head == NULL)
	{
		printf("Deque is empty\n");
	}
	printf("The element at the last of deque is %d.\n\n", last->data);
}	//O(1) time complexity

void isEmpty()	//Function to know whether deque is empty or not
{
	if (head == NULL)
	{
		printf("List is empty.\n\n");
	}
	else
	{
		printf("No, list is not empty.\n\n");
	}
}	//O(1) time complexity

void displayTheDeque()	//Function to print the whole deque
{
	if (head == NULL)
	{
		printf("Deque is empty.\n\n");
	}
	else
	{
		printf("The Deque is \n\t ");
		printf("Front-----> ");
		struct Deque *temp = head;	//initializing the temporary pointer to head of deque
		while (temp != NULL)
		{
			printf("%d  \t", temp->data);
			temp = temp->next;
		}
		printf(" <-----End\n\n");
	}
}	//O(n) time complexity

int main()
{
	struct Deque *root = NULL;
	root = createDeque(root, 4);	//creating Deque
	push_front(root, 6);	//pushing data on the front
	push_back(root, 5);	//pushing data on the back
	push_front(root, 61);
	push_front(root, 6);
	push_front(root, 12);
	push_front(root, 60);
	push_back(root, 68);
	displayTheDeque();	//Displaying the deque
	pop_front();	//removing front element
	printf("After removing from front, ");
	displayTheDeque();
	pop_back();	//removing back element
	printf("After removing from back, ");
	displayTheDeque();
	front();	//Getting value of front element of deque
	back();	//Getting value of back element of deque
	isEmpty();	//Checking if deque is empty or not
}
