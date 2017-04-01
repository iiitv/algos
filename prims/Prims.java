public class Prims {
    private static int[] generate(int[][] ar) {
        int length = ar.length;
        // Stores the parent of each vertex
        int parent[] = new int[length];
        // key value of each vertex
        int key[] = new int[length];
        // Flag for included in the MST
        boolean mstSet[] = new boolean[length];
        // Initialization of arguments
        for (int i = 0; i < length; i++) {
            mstSet[i] = false;
            key[i] = Integer.MAX_VALUE;
        }

        // Starting from the first vertex
        // As the first vertex is the root
        // So it doesn't have any parent
        key[0] = 0;
        parent[0] = -1;

        for (int i = 0; i < length - 1; i++) {
            // minimum key from given vertices
            int u = minKey(key, mstSet);
            mstSet[u] = true;

            // Updating the neighbours key
            for (int j = 0; j < length; j++) {
                if (ar[u][j] != 0 && !mstSet[j] && ar[u][j] < key[j]) {
                    parent[j] = u;
                    key[j] = ar[u][j];
                }
            }

        }

        return parent;
    }

    private static int minKey(int[] key, boolean[] visited) {
        int min = Integer.MAX_VALUE;
        int minIdx = -1;
        int length = key.length;
        for (int i = 0; i < length; i++) {
            if (!visited[i] && key[i] < min) {
                min = key[i];
                minIdx = i;
            }
        }
        return minIdx;
    }

    public static void main(String[] args) {
        // Given graph
        int nodes[][] = new int[][] {
                {0, 2, 0, 6, 0},
                {2, 0, 3, 8, 5},
                {0, 3, 0, 0, 7},
                {6, 8, 0, 0, 9},
                {0, 5, 7, 9, 0},
        };
        // parent of all the vertices
        int parent[] = generate(nodes);
        int length = nodes.length;

        // printing the MST (Prism Algorithm)
        System.out.println("Edge : Weight");
        for (int i = 1; i < length; i++) {
            System.out.println(parent[i] + " - " + i + " : " + nodes[i][parent[i]]);
        }
    }

}

