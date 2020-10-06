// Algorithm to find the bridges in graph
// A bridge is an edge in graph which after removing distribute the graph in connected components

#include<bits/stdc++.h>
using namespace std;

// adjacency list(graph)
vector<int> g[100001];

vector<bool> vis;
vector<int> tin,low;
int timer;

void dfs(int v,int p=-1){
	vis[v]=true;
	tin[v]=low[v]=timer++;
	for(int x:g[v]){
		if(x==p) continue;
		if(vis[x]){
			low[v]=min(low[v],tin[x]);
		}
		else
		{
			dfs(x,v);
			low[v]=min(low[v],low[x]);
			if(low[x]>tin[v])
			{
				bridge_found(x,v);
			}
		}
	}
}

void find_bridges(int n){
	timer=0;
	tin.assign(n+1,-1);
	low.assign(n+1,-1);
	vis.assign(n+1,false);
	for(int i=1;i<=n;i++){
		if(!vis[i])
		dfs(i);
	}
}

void bridge_found(int a,int b){
    cout<<" The Bridge is found between "<<a<<" "<<b<<"\n";
}

int main(){
    int n,q; // n is number of nodes ,q is number of edges in a graph
    cin>>n>>q;
    while(q--){
    	int u,v;
    	cin>>u>>v;
    	g[u].push_back(v);
    	g[v].push_back(u);
    }
  
    find_bridges(n);
    return 0;
}
