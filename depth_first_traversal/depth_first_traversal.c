#include <stdio.h>

/* Program to perform depth first search over a graph with a specific start node.
 */

/* 
 @ar - graph represeantation using adjency matrix
 @visited - array to mark the visited nodes
 @size - size of the array
 */
 
void depth_first_search(int ar[5][5], int *visited, int start, int size) {
	
	visited[start] = 1;
	printf("node: %d\n", start);
	
	for ( int j=0; j<size; j++) {
      if(ar[start][j] == 1 && visited[j]==0) {
					
			depth_first_search(ar, visited, j, size);
			
		}
			
	}
	
}

int main() {
	
	int ar[5][5] = { {0, 1, 0, 0, 0}, 
	                 {1, 0, 1, 0, 0},
	                 {0, 0, 0, 1, 0},
	                 {0, 0, 0, 0, 1},
	                 {0, 0, 0, 0, 0}
	                };
	
	int visited[5] = {0, 0, 0, 0, 0};
	
	int start = 0;
	
	depth_first_search(ar, visited, start, 5);
	
	return 0;
}
