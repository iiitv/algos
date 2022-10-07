//Disjoint Set Data Structure
public class DisjointUnionSet {
    int[] rank, parent;
    int size;

    // Parameterized constructor
    public DisjointUnionSet(int size) {
        parent = new int[size];
        rank = new int[size];
        this.size = size;
        init();
    }

    /**
     * 
     * @param val
     * @return representative of set to which val belongs
     */
    public int find(int val) {
        if (this.parent[val] == val) // if val is parent of itself then return val
            return val;
        // if val is not parent of itself Then
        // val is not the representative of set to which it belongs
        // hence recursively call find on val's parent
        // while performing the path compression
        return this.parent[val] = find(this.parent[val]);
    }

    /**
     * Unites the set that includes val1 and set that includes val2
     * 
     * @param val1 element of first set
     * @param val2 element of second set
     */
    public void union(int val1, int val2) {
        // Find representatives of set to which val1 and val2 belongs
        int val1Representative = find(val1);
        int val2Representative = find(val2);

        // Elements belong to same set, return
        if (val1Representative == val2Representative)
            return;

        // if val1's representative rank is less than val2's representative
        if (rank[val1Representative] < rank[val2Representative])
            // Move val2 under val1 so depth of tree remains less
            this.parent[val1Representative] = val2Representative;

        // else if val1's representative rank is less than val2's representative
        else if (this.rank[val2Representative] < this.rank[val1Representative])
            // Move val1 under val2 so depth of tree remains less
            this.parent[val2Representative] = val1Representative;

        // if the ranks are same
        else {
            // move val1 under val2
            parent[val2Representative] = val1Representative;
            // increment resultant tree rank by 1
            rank[val1Representative] += 1;

        }

    }

    /**
     * initializes the parent array
     */
    private void init() {
        for (int i = 0; i < this.size; i++) {
            parent[i] = i; // initially all the elements are in their own set
        }
    }

}

// Driver code
class Main {
    public static void main(String[] args) {
        // create a dsu for 5 elements
        DisjointUnionSet dsu = new DisjointUnionSet(5);

        System.out.println("Representative of 1 is :" + dsu.find(1)); // get representative of 1
        System.out.println("Representative of 2 is :" + dsu.find(2)); // get representative of 2


        System.out.println("\nApplying union on set to which 1 and 2 belong\n");
        dsu.union(1, 2); // do union of of set to which 1 and 2 belongs

        System.out.println("Representative of 1 is :" + dsu.find(1)); // get representative of 1
        System.out.println("Representative of 2 is :" + dsu.find(2)); // get representative of 2

    }
}