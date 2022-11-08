#include<bits/stdc++.h>
using namespace std;

// adjacency list
vector<int> graph[100001];

// visited array
bool visited[100001];

void DFS(int u){
    visited[u] = true;

    // do something
    cout<<u<<" ";

    for (int x: graph[u]){
        if(!visited[x]){
            visited[x] = true;
            DFS(x);
        }
    }
}

int main(){
    int numberofNodes;
    cin>>numberofNodes;

    int numberofEdges;
    cin>>numberofEdges;

    while(numberofEdges--){
        int u,v;
        // edge between node u & node v
        cin>>u>>v;

        g[u].push_back(v);
        g[v].push_back(u);
    }
    memset(visited, false, sizeof(visited));
    
    DFS(0);

}