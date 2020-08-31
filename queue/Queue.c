#include<stdio.h>
#include<stdlib.h>
#define MAX 5
int Q[MAX];
int front=-1;int rear=-1;
void enqueue(int x)
{
	if(rear==MAX-1)
		printf("queue overflow\n");
	else{
		if(front==-1 && rear==-1)
		{
			front=0;
			rear=0;
			Q[rear]=x;
		}
		else
			Q[++rear]=x;
	}
}
int dequeue()
{
	int t;
	if(front==-1 && front>rear)
		printf("queue underflow\n");
	else
	{
		if (front==rear)
		{
			t=Q[front];
			front=rear=-1;
		}
		else
			t=Q[front++];

 	}
 	return t;
}

void display()
{
	if(front==-1 || front>rear)
		printf("queue empty\n");
	else
		for(int i=front;i<=rear;i++)
			printf("%3d",Q[i]);
}

void main()
{	int n,x;
	while(1)
	{

	printf("1.Enqueue\n");
	printf("2.Dequeue\n");
	printf("3.Display\n");
	printf("4.Exit\n");
	scanf("%d",&n);

	switch(n){
	case 1:                                                                                                                                                                     
		printf("enter the element to enqueue:\n");
		scanf("%d",&x);
		enqueue(x);
		break;
	case 2:
	printf("Dequeueing\n");
	int x=dequeue();
	printf("Dequeued element is %d \n",x);
		break;

	case 3:
	display();
	printf("\n");
	break;

	case 4:
	exit(1);
	
	default:
	printf("wrong choice\n");
}








}}