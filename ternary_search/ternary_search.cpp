#include <iostream>

using namespace std;
/*
 * Function implementing ternary search
 * args:
 *		ar		: Initial array containing elements (unsorted)
 *		n		: the search tree's depth
 *		left : left index of array.
 *		right : right index of array.
 *		x : element to be searched.
 * Time Complexity : O(max(input))
 */  
int ternary_search (int ar[],int n, int left, int right, int x){

    if(left < 0 || right > n-1 || left > right){
        return -1;
    }
    if(x == ar[left]){
        return left;
    }

    if(x == ar[right]){
        return right;
    }

   // Update the two index left and right if the element is not found.


    if(x < ar[left]){
        return ternary_search(ar,n,left-1,right,x);
    }

    if (x > ar[left] && x < ar[right]){
        return ternary_search(ar,n,left+1,right-1,x);
    }

    if(x > ar[right]){
        return ternary_search(ar,n,left,right+1,x);
    }
}


int main(){
	int s = 12;
    int v[s];
    short x;
    for(int i = 1; i <= s; i++){
        v[i-1] = i;
    }
    cout << "Enter number for research:\n";
    cin >> x;

    int left = s/3;
    int right = (s/3)*2;

    if(ternary_search(v,s,left-1,right-1,x) == -1){
        cout<<"Number does not exist in array.\n";
    }else{
        cout<<"The index is:"<<ternary_search(v,s,left-1,right-1,x)<<"\n";
    }
    return 0;
}
