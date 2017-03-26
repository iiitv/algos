class DepthFirstTraversal {

    public static int[] arr;    // DFS traversal path
    public static int k = 0;
    public static void depthFirstTraversal(int a[][], int visited[], int i, int n) {
        arr[k] = i + 1;
        k++;
        visited[i] = 1;    // mark as visit 
        for (int j = 0; j < n; j++) {
            if (a[i][j] == 1 && visited[j] == 0) {    //check connected and visited
                depthFirstTraversal(a, visited, j, n);    //recursive call
            }
        }
    }

    public static void main(String args[]) {
        int n = 5;    // No. of vertices
        int[] visited = new int[n]; 
        arr = new int[n];
        // Adjacency Matrix of graph
        int[][] a = new int[][] {{0, 1, 0, 1, 0},
                                 {0, 0, 0, 1, 1},
                                 {1, 1, 0, 1, 0},
                                 {0, 0, 0, 0, 0},
                                 {0, 0, 1, 0, 0}};
        for (int i = 0; i < n; i++) {
            visited[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                depthFirstTraversal(a, visited, i, n);
            }
        }
        for (int element : arr) {
            System.out.println(element);
        }
    }
}
