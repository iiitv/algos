import collections

def bfs(graph, root):
    returnprint = 'BFS Order: '
    seen, queue = set([root]), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        returnprint += str(vertex) + '  '
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
    print(returnprint)

def visit(n):
    print(n)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2, 0], 2: []} 
    bfs(graph, 1) # 1 2 0

    graph2 = {0: [1, 3], 1: [3, 2], 2: [2, 1], 3: []}
    bfs(graph2, 2) # 2 1 3

    graph3 = {0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [4, 0], 4: []}
    bfs(graph3, 1) # 1 2 3 4 0

    graph4 = {0: [1, 3], 1: [3, 2], 2: [2, 4], 3: [4, 3], 4: [4, 0], 5: [0, 1], 6: []}
    bfs(graph4, 0) # 0 1 3 2 4

    bfs(graph4, 2) # 2 4 0 1 3
