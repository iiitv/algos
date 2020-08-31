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
	head = (struct node *)malloc(sizeof(struct node));
	head->data = key;
	head->next = NULL;
	head->prev = NULL;
	last = head;
	return head;
}

struct node *additionOfNodeAtBeginning( int key)
{
	struct node *temp;
	temp = (struct node *)malloc(sizeof(struct node));
	temp->data = key;
	temp->next = NULL;
	temp->next = head;
	temp->prev = NULL;
	head->prev = temp;
	head = temp;
	return head;
}

struct node *additionOfNodeAtEnding( int key)
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

struct node *additionOfNodeAtRandomeIndex( int key, int index)
{
	struct node *temp;
	temp = (struct node *)malloc(sizeof(struct node));
	temp->data = key;
	temp->next = NULL;
	struct node *temp1, *temp2, previous;
	temp1 = head;
	int i = 0;
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

struct node *deletingFromBeginning()
{
	struct node *temp;
	temp = head;
	head = head->next;
	head->prev = NULL;
	free(temp);
	return head;
}

struct node *deletingFromEnding()
{
	struct node *temp, *temp2;
	temp=last->prev;
	temp2=last;
	temp->next=NULL;
	last=temp;
	free(temp2);
	return head;
}

struct node *deletingFromRandomIndex(int index)
{
	struct node *temp, *temp2;
	temp = head;
	int i = 0;
	while (i < index - 1)
	{
		i++;
		temp = temp->next;
	}
	if (temp->next == NULL)
	{
		return deletingFromEnding();
	}
	temp2 = temp->next;
	temp2->next->prev = temp;
	temp->next = temp->next->next;
	free(temp2);
	return head;
}

void displayInReverse()
{
	printf("the Linked List in Reverse Order is ");
	struct node *temp = last;
	while (temp != NULL)
	{
		printf("%d ", temp->data);
		temp = temp->prev;
	}
	printf("\n\n");
}

void display()
{
	printf("the Linked List is ");
	struct node *temp = head;
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

	root = createNode( 4);

	additionOfNodeAtBeginning(6);
	additionOfNodeAtEnding(90);
	printf("After adding 90 at last ,");
	display();
	additionOfNodeAtRandomeIndex(12,1);
	printf("After adding 12 at index 1 ,");
	display();
	additionOfNodeAtBeginning(1);
	additionOfNodeAtEnding(2);
	additionOfNodeAtBeginning(5);
	additionOfNodeAtEnding(98);
	additionOfNodeAtRandomeIndex(122,2);
	display();
	deletingFromBeginning();
	printf("After Deletion from beginning, ");
	display();
	deletingFromEnding();
	printf("After deleting from end, ");
	display();
	deletingFromRandomIndex(3);
	printf("After deleting from index 3 ,");
	display();

	displayInReverse();
}
