#include<bits/stdc++.h>
using namespace std;

vector<int> BreadthFirstSearch(int vertex,vector<int> adjacent[],int start_vertex,int destination){
	queue<int> que;
    //bfsPath will store the path
	vector<int> bfsPath;
    //this array will take care of duplicate traversing
	bool visited[vertex];
    vector<int>::iterator it;
	que.push(start_vertex);
    bfsPath.push_back(start_vertex);
	visited[start_vertex]=true;
    int flag=0;
	while(!que.empty()){
		int tem = que.front();
		que.pop();
		for(it = adjacent[tem].begin();it<adjacent[tem].end();it++){
            if(!visited[*it]){
                bfsPath.push_back(*it);
                //if destination is found
                if(*it==destination){
                    flag=1;
                    break;
                }
                visited[*it] = true;
                que.push(*it);
            }
        }
        if(flag==1){
            break;
        }
	}
    //if we will not find the destination
    if(flag==0){
        bfsPath.clear();
    }
    return bfsPath;
}

//this fn will print the path
void printTraversal(vector<int>bfsPath){
    vector<int>::iterator it;
    for(it = bfsPath.begin();it<bfsPath.end();it++){
        cout<<*it<<endl;
    }
}

int main() {
    //number of vertex
	int vertex = 4;
	vector<int> adjacent[vertex];
	adjacent[0].push_back(1);
	adjacent[0].push_back(3);
	adjacent[1].push_back(2);
	adjacent[2].push_back(3);
    //starting vertex
	int start_vertex = 0;
    //destination
    int destination = 3;
	vector<int> bfsPath = BreadthFirstSearch(vertex,adjacent,start_vertex,destination);
    if(!bfsPath.empty()){
    printTraversal(bfsPath);
    }else{
        cout<<"path not found";
    }
    return 0;
}

