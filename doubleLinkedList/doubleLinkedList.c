#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *next;
	struct node *prev;
};

struct node *head = NULL, *last = NULL;

struct node *createNode(int key)
{
	head = (struct node *)malloc(sizeof(struct node)); //allocate the required space to *node variable
	head->data = key;
	head->next = NULL;
	head->prev = NULL;
	last = head;
	return head;
}

struct node *additionOfNodeAtBeginning(int key) //adding at the beginning of the linked list
{
	struct node *temp;
	temp = (struct node *)malloc(sizeof(struct node));
	temp->data = key;
	temp->next = head; //making temp variable point to head of the linked list
	temp->prev = NULL; //pointing the prev of temp to NULL pointer
	head->prev = temp;
	head = temp;
	return head;
}

struct node *additionOfNodeAtEnding(int key) //adding the element at the last of the linked list
{
	struct node *temp;
	temp = (struct node *)malloc(sizeof(struct node));
	temp->data = key;
	temp->next = NULL;
	temp->prev = last;
	last->next = temp;
	temp->next = NULL;
	last = temp;
	return last;
}

struct node *additionOfNodeAtRandomeIndex(int key, int index) //adding the element at the given index
{
	struct node *temp;
	temp = (struct node *)malloc(sizeof(struct node));
	temp->data = key;
	temp->next = NULL;
	if (index == 0)
	{
		return additionOfNodeAtBeginning(key);
	}
	struct node *temp1, *temp2;
	temp1 = head;
	int i = 0;
	//iterating through the list till the iterator variable is index or list is empty
	while (i < index - 1 && temp1->next != NULL)
	{
		temp1 = temp1->next;
		i++;
	}
	if (temp1->next == NULL)
	{
		additionOfNodeAtEnding(key);
	}
	temp2 = temp1->next;
	temp->prev = temp1;
	temp1->next = temp;
	temp->next = temp2;
	temp2->prev = temp;
	return head;
}

struct node *deletingFromBeginning() //deleting the element at head
{
	struct node *temp;
	temp = head;
	head = head->next; //making the head pointer to point the element next to it
	head->prev = NULL;
	free(temp); //free the space occupied by former head pointer
	return head;
}

struct node *deletingFromEnding() //deleting the element from the ending
{
	struct node *temp, *temp2;
	temp = last->prev; //temp pointer pointing to the second last element of linked list
	temp2 = last;	   //temp2 pointing to last element
	temp->next = NULL;
	last = temp; //make second last pointer as last element
	free(temp2);
	return head;
}

struct node *deletingFromRandomIndex(int index) //deleting the element from given index
{
	struct node *temp, *temp2;
	temp = head;
	int i = 0;
	while (temp != NULL && i < index)
	{
		i++;
		temp = temp->next;
	}
	if (index == 0)
	{
		return deletingFromBeginning();
	}
	else if (temp == last)
	{
		return deletingFromEnding();
	}
	else if (temp != NULL) //if temp is NULL the index is out of Bound
	{
		temp->prev->next = temp->next;
		temp->next->prev = temp->prev;
		free(temp);
	}
	else
	{
		printf("Index Out Of Bound\n"); //index is out of bound
	}
	return head;
}

void displayInReverse() //display the linked list in reverse order
{
	printf("the Linked List in Reverse Order is ");
	struct node *temp = last; //creating iterator pointing to the last element
	while (temp != NULL)
	{
		printf("%d ", temp->data);
		temp = temp->prev;
	}
	printf("\n\n");
}

void display() //display the linked list
{
	printf("the Linked List is ");
	struct node *temp = head; //creating iterator pointing to the head
	while (temp != NULL)
	{
		printf("%d ", temp->data);
		temp = temp->next;
	}
	printf("\n\n");
}

int main()
{
	struct node *root = NULL;
	root = createNode(4); // creating the list

	additionOfNodeAtBeginning(6); //adding the value 6 at beginning
	additionOfNodeAtEnding(90);	  //adding value 90 at last
	printf("After adding 90 at last ,");
	display(); //display the list
	//index are starting from 0
	additionOfNodeAtRandomeIndex(12, 1); //adding 12 at index 1
	printf("After adding 12 at index 1 ,");
	display();
	additionOfNodeAtBeginning(1);
	additionOfNodeAtEnding(2);
	additionOfNodeAtBeginning(5);
	additionOfNodeAtEnding(98);
	additionOfNodeAtRandomeIndex(122, 2); //index are starting from 0
	display();
	deletingFromBeginning(); //deleting the head element
	printf("After Deletion from beginning, ");
	display();
	deletingFromEnding(); //deleting the last element from the list
	printf("After deleting from end, ");
	display();
	deletingFromRandomIndex(3); //deleting the element at index 3(0 is starting index)
	printf("After deleting from index 3 ,");
	display();

	displayInReverse(); //display the linked list in reverse order
}
