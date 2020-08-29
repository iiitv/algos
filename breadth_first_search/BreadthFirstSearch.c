/* breadth first search is a traversal technique used for graphs. First a starting vertex is picked and all the adjacent to the starting
vertex are traversed. And this process goes on.
This process is similar to level order traversal of trees */

#include <stdio.h>
#include <stdlib.h>
int N; // no of vertices in a graph
int adj[100][100]={0}; // adjacency matrix
int state[100]; //state of a node whether it is at initial, waiting or at visited stage
void BFS_traversal(); 
void BFS(int a);
int queue[100];
int front = -1,rear = -1;
void insert(int vertex);
int delete_queue();
int isempty();
void BFS_traversal(){
	int v;
	for(v=0;v<N;v++)
		state[v] = 1;
	printf("Enter starting vertex for breadth first search : ");
	scanf("%d",&v);
	BFS(v);
}
void BFS(int v){
	int i;
	insert(v);
	state[v]=2;
	while(!isempty())
	{
		v = delete_queue();
		printf("%d ",v);
		state[v]=3;
		for(i=0;i<N;i++)
		{
			if(adj[v][i]==1 && state[i]==1)
			{
				insert(i);
				state[i]=2;
			}
		}
		printf("\n");
	}
}
void insert(int vertex){
	if(rear==100-1)
		printf("Queue overflow\n");
	else
	{
		if(front==-1)
			front=0;
		rear = rear + 1;
		queue[rear] = vertex;
	}
}
int isempty(){
	if(front == -1 || front > rear)
		return 1;
	else
		return 0;
}
int delete_queue(){
	int deleteitem;
	if(front==-1 || front>rear)
	{
		printf("Queue underflow\n");
		exit(1);
	}
	deleteitem = queue[front];
	front = front - 1;
	return deleteitem;
}
int main()
{
	N = 4;
	adj[0][1]=1;
	adj[0][3]=1;
	adj[1][0]=1;
	adj[1][2]=1;
	adj[1][3]=1;
	adj[2][3]=1;
	adj[3][1]=1;
	BFS_traversal();
}
