#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
int tree[200002];
int MaxVal=200002;

int read(int idx){
    if(idx==0)return 0;
	int sum = 0;
	while (idx > 0){
		sum += tree[idx];
		idx -= (idx & -idx);
	}
	return sum;
}

void update(int idx ,int val){
	while (idx <= MaxVal){
		tree[idx] += val;
		idx += (idx & -idx);
	}
}

int main(){

  memset(tree,0,sizeof(tree));
	update(3,1);
	update(4,1);
	cout<<read(5)<<endl;
	update(10,2);
	update(8,3);
	cout<<read(9)<<endl;
	
    return 0;
}

