package algos.Disjoint_Union_Set;

public class DisjointUnionSet {

    public int find(int a,int parent[])//recursive function to find parent of a 
    {
        if(parent[a]==a)//if root itself is a parent
        return a;
        else
        return find(parent[a],parent);//to find the parent of the parent
    }
    public void union(int a,int b,int parent[],int rank[])//function to do union of a and b
    {
       int a1=find(a,parent);//to find parent of a
       int b1=find(b,parent);//to find parent of b
       if(a1==b1)//if both have same parent that is both are in same set
       {System.out.println("both the elements are in same set");
       return;}
       if(rank[a1]>rank[b1])//if height of parent of a is greater than height of parent of b
       {
           parent[b1]=a1;
       }
       else if(rank[a1]<rank[b1])//if height of parent of b is greater than height of parent of a
       {
           parent[a1]=b1;
       }
       else//if height of both parent is same 
       {
           parent[a1]=b1;
           rank[b1]++;
       }
    }
    public static void main(String args[])
    {
        int n=10;
        int parent[]=new int[n];
        int rank[]=new int[n];

        for(int i=0;i<10;i++)
        parent[i]=i;//in starting the node is itself the parent 
        for(int i=0;i<10;i++)
        rank[i]=1;//by default the rank of all nodes is 1

        DisjointUnionSet dsu=new DisjointUnionSet();
        dsu.union(3,8,parent,rank);//3 is friend of 8
        dsu.union(3,6,parent,rank);//3 is friend of 6
        System.out.println("the parent of 8 is"+dsu.find(8,parent));
        
        dsu.union(1,9,parent,rank);//1 is friend of 9
        dsu.union(2,8,parent,rank);//2 is friend of 8
        dsu.union(5,8,parent,rank);//5 is friend of 8

        dsu.union(2,9,parent,rank);//2 is friend of 9
        System.out.println("the parent of 2 is"+dsu.find(2,parent));
        System.out.println("the parent of 8 is"+dsu.find(8,parent));

        if(dsu.find(5,parent)==dsu.find(7,parent))//to check whether 5 is friend of 7 or not 
        System.out.println("5 is a friend of 7");
        else  System.out.println("5 is not a friend of 7");

        if(dsu.find(3,parent)==dsu.find(1,parent))//to check whether 3 is friend of 1 or not 
        System.out.println("3 is a friend of 1");
        else  System.out.println("3 is not a friend of 1");





    }


    
}