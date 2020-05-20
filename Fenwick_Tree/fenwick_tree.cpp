// c++ implimentation of BIT(Binary Indexed Tree aka Fenwick Tree)
// These type of tree implimentation is used to answer ranged query in O(log n) time
// Total running time = O(n log n)  -> n*log n for building the tree and Q*log n for answering Q queries


// NOTE : This is indexing one based fenwick tree
#include <bits/stdc++.h>

using namespace std;
int n;
vector<int> FTree;
int arr[100009];

void buildTree();
int getnext(int index);
void UpdateTree(int idx, int val);
int query(int idx);
int RangeQuery(int l,int r);
int getparent(int child);

int getparent(int child)
{
    return child - (child & -child);
}

int getnext(int index)
{
    return index + (index & -index);
}

void UpdateTree(int idx, int val)
{
    if(idx > n)
    {
        return;
    }
    FTree[idx]+=val;
    UpdateTree(getnext(idx),val);
}

void buildTree()
{
    for(int i=1;i<=n;i++)
    {
        UpdateTree(i,arr[i]);
    }
}

int query(int idx)
{
    if(idx<=0)
    {
        return 0;
    }
    return FTree[idx]+query(getparent(idx));

}

int RangeQuery(int l,int r)
{
    return (query(r)-query(l-1));
}

//driver function
int main()
{
    
    cin >>n; //Length of the array, lets take n=10 for example {2,3,4,1,4,5,3,2,1,9}
    FTree.assign(n+1,0); // assigning 0 to all the nodes of the tree
    for(int i=1;i<=n;i++)
    {
        cin >>arr[i];
    }
    buildTree();
    // printing out a sample answer for a query from index [4,9] it's answer should be 16
    int Q; // number of queries
    cin >>Q;
    for(int i=0;i<Q;i++)
    {
        int l,r;
        cin >>l>>r;
        cout <<RangeQuery(l,r);
    }
    return 0;
}