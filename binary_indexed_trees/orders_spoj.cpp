#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
int tree[200002];
int MaxVal=200001;

int read(int idx){
    if(idx==0)return 0;
	int sum = 0;
	while (idx > 0){
		sum += tree[idx];
		idx -= (idx & -idx);
	}
	return sum;
}


int get(int sum){
    int idx=1<<17;
    int ac=0;
    
    while(idx!=0){     
        if(ac+idx>MaxVal || tree[ac+idx]>= sum){
            idx>>=1;
        }else{
            sum-=tree[ac+idx];
            ac+=idx;
            idx>>=1;    
        }
    }
    
    return ac+1;
}


void update(int idx ,int val){
	while (idx <= MaxVal){
		tree[idx] += val;
		idx += (idx & -idx);
	}
}

int main(){
    
    int tc;
    scanf("%d",&tc);

    while(tc--){
        memset(tree,0,sizeof(tree));
        int n;
        scanf("%d",&n);
        int c[n];
        
        for(int i=0;i<n;i++)
            scanf("%d",&c[i]);
        
        for(int i=0;i<n;i++)
            update(i+1,1);
        
        int val=n;
        int dev[n];
        for(int i=n-1;i>=0;i--){
            dev[i]=get(val-c[i]);
            update(dev[i],-1);
            val--;
        }
        
        for(int i=0;i<n;i++){
            if(i!=n-1)printf("%d ",dev[i]);    
            else printf("%d",dev[i]);
        }
        
        printf("\n");
    }
    
    return 0;
}
