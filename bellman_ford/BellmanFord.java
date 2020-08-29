
class BellmanFord {
    // A nested edge class to declare source destination and weight of an edge
    class Edge {
        int src, dest, weight;

        Edge() {
            src = 0;
            dest = 0;
            weight = 0;
        }
    };

    int Vertices, Edges;
    Edge edge[];

    // Constructor to create a graph with a given nodes and edges
    BellmanFord(int vertices, int edges) {
        Vertices = vertices;
        Edges = edges;
        edge = new Edge[Edges];
        for (int i = 0; i < Edges; i++) {
            edge[i] = new Edge();
        }
    }

    // To print the minimus distances from the source
    void printArray(int distanceFromSrc[], int Source) {
        System.out.println("Minimum Distance from the node " + (Source + 1) + " is: -");
        for (int i = 0; i < Vertices; i++) {
            System.out.println("Node " + (i + 1) + " " + distanceFromSrc[i]);
        }
    }

    void bellmanFordAlgo(BellmanFord graph, int src) {
        int Vertices = graph.Vertices;
        int Edges = graph.Edges;

        int distanceFromSrc[] = new int[Vertices];

        // Initializing the distance array with Infinity
        for (int i = 0; i < Vertices; i++) {
            distanceFromSrc[i] = Integer.MAX_VALUE;
        }

        distanceFromSrc[src] = 0;
        // Relaxing all edges for Vertices-1 times
        for (int i = 0; i < Vertices - 1; i++) {

            for (int j = 0; j < Edges; j++) {
                int currentEdgeSrc = graph.edge[j].src;
                int currentEdgeDest = graph.edge[j].dest;
                int currentEdgeWeight = graph.edge[j].weight;

                if (distanceFromSrc[currentEdgeSrc] != Integer.MAX_VALUE
                        && (distanceFromSrc[currentEdgeSrc] + currentEdgeWeight) < distanceFromSrc[currentEdgeDest]) {
                    distanceFromSrc[currentEdgeDest] = distanceFromSrc[currentEdgeSrc] + currentEdgeWeight;// Relaxing

                }
            }
        }
        // Checking for a negative weight cycle
        for (int j = 0; j < Edges; j++) {
            int currentEdgeSrc = graph.edge[j].src;
            int currentEdgeDest = graph.edge[j].dest;
            int currentEdgeWeight = graph.edge[j].weight;
            if (distanceFromSrc[currentEdgeSrc] != Integer.MAX_VALUE
                    && distanceFromSrc[currentEdgeSrc] + currentEdgeWeight < distanceFromSrc[currentEdgeDest]) {
                System.out.println("Graph has negative weight cycle, Failed");
                return;
            }
        }

        printArray(distanceFromSrc, src);

    }

    public static void main(String args[]) {
        int Vertices = 7;
        int Edges = 10;
        BellmanFord graph = new BellmanFord(Vertices, Edges);

        int src = 0;
        // Creating the graph
        graph.edge[0].src = 0;
        graph.edge[0].dest = 1;
        graph.edge[0].weight = 6;

        graph.edge[1].src = 0;
        graph.edge[1].dest = 2;
        graph.edge[1].weight = 5;

        graph.edge[2].src = 0;
        graph.edge[2].dest = 3;
        graph.edge[2].weight = 5;

        graph.edge[3].src = 3;
        graph.edge[3].dest = 2;
        graph.edge[3].weight = -2;

        graph.edge[4].src = 2;
        graph.edge[4].dest = 1;
        graph.edge[4].weight = -2;

        graph.edge[5].src = 1;
        graph.edge[5].dest = 4;
        graph.edge[5].weight = -1;

        graph.edge[6].src = 2;
        graph.edge[6].dest = 4;
        graph.edge[6].weight = 1;

        graph.edge[7].src = 3;
        graph.edge[7].dest = 5;
        graph.edge[7].weight = -1;

        graph.edge[8].src = 5;
        graph.edge[8].dest = 6;
        graph.edge[8].weight = 3;

        graph.edge[9].src = 4;
        graph.edge[9].dest = 6;
        graph.edge[9].weight = 3;

        graph.bellmanFordAlgo(graph, src);
    }

}
