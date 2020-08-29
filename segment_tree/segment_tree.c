//implement a segment tree in C

#include <stdlib.h>
#include<stdio.h>
#include<math.h>
#define ll               long long int
#define loop(a,b,i)      for(ll i=a;i<b;i++)
#define loop1(a,b,i)     for(ll i=a;i>b;i--)
//using namespace std;

ll min(ll a,ll b )//min function to compute minimum of 2 values
{
    if(a<b)return a;
    return b;
}
void build(ll left,ll right,ll tree[],ll arr[],ll index)//to recursively contruct the segment tree in O(n)
{
    if(left==right)
    {tree[index]=arr[left]; return;}
    else
    {
        ll mid=(left+right)/2;
        build(left,mid,tree,arr,2*index+1);//to build the left subtree
        build(mid+1,right,tree,arr,2*index+2);//to build the right subtree
        tree[index]=min(tree[2*index+1],tree[2*index+2]);// to build the parent node of left and right subtree.
        return;
    }

}
void update(ll left,ll right,ll tree[],ll arr[],ll index,ll ind,ll value)//to update a given value at a particular index in O(logn)
{
    if(right<ind||left>ind)
    return;

    if(left==right&&left==ind)
    {tree[index]=value;return ;}

    ll mid=(left+right)/2;
    update(left,mid,tree,arr,2*index+1,ind,value);
    update(mid+1,right,tree,arr,2*index+2,ind,value);
    tree[index]=min(tree[2*index+1],tree[2*index+2]);

}
ll ans(ll left,ll right,ll initial,ll final,ll tree[],ll arr[],ll index)// to provide the minimum value within a given range in O(logn)
{
    if(left<=initial&&right>=final)
    return tree[index];
    if(right<initial||left>final)
    return 1e18;
    
    ll mid=(initial+final)/2;
    return min( ans(left,right,initial,mid,tree,arr,2*index+1) , ans(left,right,mid+1,final,tree,arr,2*index+2) ) ;
}
int main() {
  
    ll tc=1;
   
    while(tc--)
    {
        ll n;
     
        ll arr[]={9,4,5,3,6,2,10};
        n=7;
     
        ll tree[12]={0};//to contruct a seg tree in the form of array 
        build(0,n-1,tree,arr,0);//to construct segment tree in O(n)

        ll l=1,r=5;
       printf("the min value in the range 1 to 5 inclusive is:%ld\n" ,ans(l-1,r-1,0,n-1,tree,arr,0));

       ll ind=3,value=-20;
       update(0,n-1,tree,arr,0,ind-1,value);//to update the value at index ind in array,thereby updating whole tree

        printf("the new min value in the range 1 to 5 inclusive is:%ld\n" ,ans(l-1,r-1,0,n-1,tree,arr,0));

       

        
    }
}