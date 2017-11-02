#include<stdio.h>
#include<stdlib.h>

struct Node{
  int data;
  struct Node *next;
};

void deque();

typedef struct Node node;


void main()
{
  struct Node *front = NULL,*rear = NULL,*temp,*front1;
  int element,choice,count=0;

  while(1){
    printf("\n1)Inserting a Node \n2)Deleting a node  \n3)Print the queue \n4)Size of queue \n5)Exit");
    printf("\nEnter your choice \n");
    scanf("%d",&choice);
    
      switch (choice)
      {
        case 1: printf("Enter the element to insert \n");
                scanf("%d",&element);
                if (rear == NULL)
                {
                  rear = (node*)malloc(sizeof(node));
                  rear->next = NULL;
                  rear->data = element;
                  front = rear;
                 }
                 else{
                  temp = (node*)malloc(sizeof(node));
                  rear->next = temp;
                  temp ->data = element;
                  temp->next = NULL;
                  rear = temp;
                 }
                 count++;
                break;
        case 2:  front1 = front;
               
                  if (front1 == NULL)
                  {
                      printf("\n Error: Trying to display elements from empty queue");
                      return;
                  }
                  else
                      if (front1->next != NULL)
                      {
                          front1 = front1->next;
                          printf("\n Dequed value : %d", front->data);
                          free(front);
                          front = front1;
                      }
                      else
                      {
                          printf("\n Dequed value : %d", front->data);
                          free(front);
                          front = NULL;
                          rear = NULL;
                      }
                      count--;
                break;

          case 3: temp = front;
                  while(temp != NULL)
                  {
                    printf("%d ->",temp->data);
                    temp = temp->next;
                  }
                  break;

          case 4:printf("No of elements : %d",count);
                 break;

          case 5: exit(7);
                  break;
      }
      
    }
}



// void deque()
// {
//   clone_front = front;
//   if (clone_front == NULL){
//     printf("No elements are present in linked list\n");
//   }
//   else if(clone_front !=NULL)
//   {
//     clone_front = front->next;
//     printf("Deleted element is: %d",front->data);
//     free(front);
//     if(clone_front->next==NULL){
//       front->next = NULL;
//       rear->next = NULL;
//     }
//   }

// }

