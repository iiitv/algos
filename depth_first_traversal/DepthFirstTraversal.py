def depthFirstTraversal(graph, node, visited):
    if node not in visited:
        visited.append(node)
        childs = graph[node]
        if len(childs) > 0:
            for child in childs:
                depthFirstTraversal(graph, child, visited)
    return visited


def main():
    graph = {'A': ['B', 'C', 'E'],
             'B': ['D', 'F'],
             'C': ['G'],
             'D': [],
             'E': ['F'],
             'F': ['C'],
             'G': []}
    result = depthFirstTraversal(graph, 'A', [])
    for node in result:
        print(node)


if __name__ == '__main__':
    main()
