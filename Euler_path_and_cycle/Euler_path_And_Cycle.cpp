
#include<bits/stdc++.h>
using namespace std;

vector<int>v[1000];

   void dfs(int u, int vis[])// a recursive depth first search
    {
        vis[u] = 1;// visit the node
        for (int i : v[u]) {
            if (vis[i] == 0)// if not visited
            {
                dfs(i, vis);// explore it
            }
        }
    }
   int isConnected(int u, int vis[], int n)// to check whether the graph is connected or not
    {
        int i = 0;
        for (; i < n; i++)
            if (v[i].size() != 0)// if node has no edges
                break;
        if (i == n)// if all the nodes are disconnected
            return 1;
        for (int j = 0; j < n; j++)
            vis[j] = 0;
        dfs(0, vis);
        for (int j = 0; j < n; j++)
            if (vis[i] == 0 && v[i].size() > 0)// to check if the graph is not conncted
                return 0;
        return 1;// if graph is connected
    }
   int isPath(int u, int vis[], int n)// to check whether euler path exist or not
    {
        int odd = 0;
        if (isConnected(u, vis, n) == 0)// to check connected or not
        {

            return 0;
        }
        for (int i = 0; i < n; i++) {
            if (v[i].size() % 2 != 0)// to count the total number of nodes with odd degrees
                odd++;
        }

        if (odd > 2)// if graph is not eulerian
            return 0;
        if (odd == 2)// if graph has euler path
            return 1;
        return 2;// if graph has euler cylce
    }
 int main() {
        int n;
        n = 5;
        // Euler_Path_And_Cycle eg1 = new Euler_Path_And_Cycle();
        // Euler_Path_And_Cycle eg2 = new Euler_Path_And_Cycle();


        int vis1[10] ={0};// visited array


        v[0].push_back(1);
        v[1].push_back(2);
        v[6].push_back(8);
        v[8].push_back(6);
        v[5].push_back(0);
        v[0].push_back(5);
        v[1].push_back(0);
        v[0].push_back(1);

        if (isPath(0, vis1, n) == 0)
          cout<<"Graph is not euler"<<endl;
        else if (isPath(0, vis1, n) == 1)
          cout<<"Graph has eular path";
        else
          cout<<"Graph has eular cycle";
		  cout<<endl;

     for(int i=0;i<=10;i++)
	 v[i].clear();

		v[2].push_back(1);
		v[1].push_back(2);
		v[0].push_back(3);
		v[3].push_back(0);
		v[4].push_back(0);
		v[0].push_back(4);

        int vis2[12] ={0}; // visited array

        if (isPath(0, vis2, n) == 0)
          cout<<"Graph is not euler";
        else if (isPath(0, vis2, n) == 1)
          cout<<"Graph has eular path";
        else
          cout<<"Graph has eular cycle";
		  cout<<endl;

	return 0;

    }

