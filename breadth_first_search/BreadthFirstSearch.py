def breadthFirstSearch(graph, first_node):
    next_nodes = [first_node]
    visited = []
    while len(next_nodes) > 0:
        node = next_nodes.pop(0)
        visited.append(node)
        childs = graph[node]
        if len(childs) > 0:
            for child in childs:
                if (child not in visited) and (child not in next_nodes):
                    next_nodes.append(child)
    return visited


def main():
    graph = {'A': ['B', 'C', 'E'],
             'B': ['D', 'F'],
             'C': ['G'],
             'D': [],
             'E': ['F'],
             'F': ['C'],
             'G': []}
    result = breadthFirstSearch(graph, 'A')
    for node in result:
        print node


if __name__ == '__main__':
    main()
