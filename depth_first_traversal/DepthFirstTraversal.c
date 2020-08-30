/* this is recursive implementation of depth first search we have three stages here named as initial, visited and finished.
At the start all the vertices are assigned initial state and after a vertex is visited its state become visited and the state of
any node or vertex becomes finished when we backtrack from it. */


#include<stdio.h>
#include<stdlib.h> 
#define MAX 100  
#define initial 1
#define visited 2
#define finished 3
int n;    
int adj[MAX][MAX];
int state[MAX]; 
void create_graph();
void DFS_Traversal();
void DFS(int v);
 
int main()
{
 create_graph();
 DFS_Traversal();
 return 0;
}
 
void DFS_Traversal()
{
 int v;
 for(v=0; v<n; v++) 
	 state[v] = initial;
 printf("Enter Start Vertex for DFS: \n");
 scanf("%d", &v);
 DFS(v);	
 for(int v=0;v<n;v++)
 {
	if(state[v]==initial)
		DFS(v);
 }
 printf("\n");
}
 
void DFS(int v)
{
 int i;
 printf("%d ",v);
 state[v] = visited;
 for(i=0;i<n;i++)
 {
	if(adj[v][i]==1 && state[i]==initial)
		DFS(i);
 }
 state[v]=finished;
}

void create_graph()
{
 int count,max_edge,origin,destin;
 printf("Enter number of vertices : ");
 scanf("%d",&n);
 max_edge = n*(n-1); 
 for(count=1; count<=max_edge; count++)
 {
	printf("Enter edge %d( -1 -1 to quit ) : ",count);
	scanf("%d %d",&origin,&destin);  
	if((origin == -1) && (destin == -1))
		break;
	if(origin>=n || destin>=n || origin<0 || destin<0)
	{
		printf("Invalid edge!\n");
		count--;
	}
	else
	{
		adj[origin][destin] = 1;
	}
 }
}
