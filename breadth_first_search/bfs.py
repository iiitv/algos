edge={}

def addEdges(source, destination):
    if(source not in edge):
        edge[source]=[]
    edge[source].append(destination)

def breadthFirstSearch(source, destination):
    bfs=[source]
    queue=[source]
    visited=[source]
    flag=0
    
    while(len(queue)!=0):
        source=queue.pop(0)
        temp=[]
        if(source in edge and len(edge[source])>0):
            temp=list(edge[source])
        for i in temp:
            if(i not in visited):
               bfs.append(i)
               if(i==destination):
                   flag=1
                   break
               queue.append(i)
               visited.append(i)

        if(flag==1):
            break;
    if(flag==0):
        return
    return bfs
    
addEdges("A", "B");
addEdges("A", "D");
addEdges("B", "C");
addEdges("C", "D");

path = breadthFirstSearch("A", "D");
if(path is None):
    print("Path not found");
else:
    print(path)
