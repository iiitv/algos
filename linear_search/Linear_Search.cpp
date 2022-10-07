#include<bits/stdc++.h>
using namespace std;
int search(int a[],int key,int n){
    for(int i = 0; i<n; i++){
        if(a[i]==key){
            return i;
        }
    }
     return -1;
}
int main(){
    int a[] = {9,7,18,1,16,10,5};
    int target = 5;
    int n = sizeof(a)/sizeof(a[0]);
    int ans = search(a,target,n);
    if(ans == -1){
        cout<<"Element doesn't exist in the array";
    }else{
        cout<<"Element is at index "<<ans;
    }
    return 0;
}

