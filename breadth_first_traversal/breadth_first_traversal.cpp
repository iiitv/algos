//@ raunak kumar jaiswal

#include <bits/stdc++.h>
using namespace std;

void bfstraversal(vector<vector<int>>& g,  vector<bool>& visited, vector<int>& ans, int node)
{
    queue<int>qq;
    qq.push(node);
    visited[node] = true;
    while(!qq.empty())
    {
        auto it = qq.front();
        qq.pop();
        for(auto itt : g[it])
        {
            if(visited[itt]==false)
            {
                visited[itt] = true;
                qq.push(itt);
            }
        }
        ans.push_back(it);
    }

}

void makegraph( vector<vector<int>>& g, int num_edge)
{
  for(int i=0;i<num_edge;i++)
  {
      int a,b;
      cin>>a>>b;
      g[a].push_back(b); 
      g[b].push_back(a);
  }
}

int main()
{
    vector<vector<int>>g;
    vector<bool>visited;
    int num_node , num_edge;
    cout<<"Enter number of Node"<<endl;
    cin>>num_node;
    cout<<"Enter number of Edges"<<endl;
    cin>>num_edge;

    g.assign(num_node,vector<int>());
    visited.assign(num_node, false);

cout<<"Enter the edges between vertex"<<endl;
    makegraph(g,num_edge);

    vector<int>ans;

    for (int i=0;i<num_node;i++)
    {
       if(visited[i]==false)
       bfstraversal(g,visited, ans, i);
    }
cout<<"----- Traversal output---"<<endl;
    for(auto it: ans)
    {
        cout<<it<<" ";
    }
    



}