// A program to print the nodes and also display the linked list in reverse order
#include<stdio.h>
#include"stdlib.h"

struct Node{
  int value;
  struct Node *next;
};

void push(struct Node **head,int element)
{
  struct Node * ptr = (struct Node *)malloc(sizeof(struct Node*));
  /* 2. put in the data  */
    ptr->value  = element;

    /* 3. Make next of new node as head */
    ptr->next = (*head);

    /* 4. move the head to point to the new node */
    (*head)    = ptr;
}

int countElements(struct Node  *ptr)
{
  struct Node *cur = ptr;
  int count=0;
  while(cur != NULL){
      count+=1;
      printf("%d ->",cur->value);
      cur = cur->next;
  }
  return count;
}

void printReverse(struct Node* head)
{
    if (head == NULL)
       return;

    printReverse(head->next);

    printf("%d  ", head->value);
}

void main()
{
      struct Node *header = NULL;
      int choice, item,a=1;
        while(a==1){
      printf("\nEnter the various choices\n1. Inseting element \n 2. Counting no of nodes\n 3. Printing the Node in reverse order \n");
      scanf("%d",&choice);
      switch(choice)
      {
        case 1: printf("Enter the element to Linked list");
                scanf("%d",&item );
                push(&header,item);
                break;
        case 2:a = countElements(header);
                printf("\nNo of nodes are : %d \n",a);
                break;
        case 3: printReverse(header);
                break;

      }

      printf("To continue input 1 :");
      scanf("%d",&a);
    }
}
