/*
 *  Below is the implementation of 'Disjoint Unoin Set' Data Structure
 *  We can also get the number of sets present at the end of all union
 *  operations.
 */

import java.util.HashSet;

class DisjointUnionSet {

    private int[] rank;
    private int[] parent;
    private int size;

    //Constructor for DisjointUnionSet class which
    //instantiates the size of the set along with parent and rank array.
    public DisjointUnionSet(int size) {
        this.size = size;
        instantiateRankArray(size);
        instantiateParentArray(size);
    }

    //Instantiate Rank array
    public void instantiateRankArray(int size) {
        rank = new int[size+1];
    }

    //Instantiate Parent array
    public void instantiateParentArray(int size) {
        parent = new int[size+1];
        for(int i=1;i<=size;i++) {
            //Initially every element act as a seperate set of single element
            parent[i] = i;
        }
    }

    //Make union of two sets which includes element1 and element 2
    public void unionSet(int element1, int element2) {
        //Find root of set including element1
        int root1 = findRoot(element1);

        //Find root of set including element2
        int root2 = findRoot(element2);

        //If we element1 and element2 belong to same set then nothing to unite
        if(root1 == root2) {
            return;
        }

        //If rank of root1 is greater than root2 then make second set as a
        //part of first set and make root1 as a root of resulting union set
        if(rank[root1] > rank[root2]) {
            parent[root2] = root1;
        }

        //Else If rank of root2 is greater than root1 then make first set as a
        //part of second set and make root2 as a root of resulting union set
        else if(rank[root1] < rank[root2]) {
            parent[root1] = root2;
        }

        //If both set has same rank then make second set as a
        //part of first set and make root1 as a root of resulting union set
        // and increment the rank of the union set
        else {
            parent[root2] = root1;
            rank[root1]++;
        }
    }

    //Returns the root of the set which element is a part of
    public int findRoot(int element) {
        if(parent[element] != element) {
            parent[element] = findRoot(parent[element]);
        }
        return parent[element];
    }

    public static void main(String[] args) {
        int size = 10;
        //Initially there are 10 sets
        DisjointUnionSet disjointSet = new DisjointUnionSet(size);

        //join 1 and 5
        disjointSet.unionSet(1,5);

        //join 1 and 9
        disjointSet.unionSet(1,9);

        //join 2 and 8
        disjointSet.unionSet(2,8);

        //join 8 and 10
        disjointSet.unionSet(8,10);

        //join 3 and 4
        disjointSet.unionSet(3,4);

        //join 4 and 7
        disjointSet.unionSet(4,7);

        //join 3 and 6
        disjointSet.unionSet(3,6);

        HashSet<Integer> sets = new HashSet<>();
        for(int i=1;i<=10;i++) {
            int currentParent = disjointSet.findRoot(i);
            System.out.println("Element: "+i+"has parent: "+currentParent);
            sets.add(currentParent);
        }
        System.out.println("Total Sets: "+sets.size());
    }
}