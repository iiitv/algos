#include<stdio.h>
#include<conio.h>
int visited[15]={0};
int adj[10][10]={999};

void main()
{int n,i,j,min,mincost=0,vertex=1,a,b;
 clrscr();
 printf("\nEnter the number of vertices in the tree:");
 scanf("%d",&n);
 printf("\nEnter the adjacency matrix:\n");
 for(i=0;i<=n-1;i++)
 {for(j=0;j<=n-1;j++)
   scanf("%d",&adj[i][j]);
 }

 vertex=1;
 visited[0]=1;
 printf("\nThe Minimum Spanning Tree is:");
 while(vertex<n)
 {for(i=0,min=999;i<n;i++)
  {for(j=0;j<n;j++)
   {if(adj[i][j]<min)
    {if(visited[i]!=0||visited[j]!=0)
     {min=adj[i][j];
      a=i;
      b=j;
     }
    }
   }
  }
  if(visited[a]==0||visited[b]==0)
  {printf("\n%d->%d\tWeight: %d",a+1,b+1,min);
   vertex++;
   mincost+=min;
   if(visited[b]==0)
    visited[b]=1;

   else visited[a]=1;
  }
  adj[a][b]=adj[b][a]=999;
 }

 printf("\nThe minimum cost is %d",mincost);
 getch();
}

/*OUTPUT

Enter the number of vertices in the tree:4                                      
                                                                                
Enter the adjacency matrix:                                                     
999 1 999 2                                                                     
1 999 4 3                                                                       
999 4 999 5                                                                     
2 3 5 999                                                                       
                                                                                
The Minimum Spanning Tree is:
1->2    Weight: 1                                                               
1->4    Weight: 2                                                               
2->3    Weight: 4                                                               
The minimum cost is 7                                                           
                                                                                
