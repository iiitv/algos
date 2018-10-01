def depthFirstTraversalRecursive(graph, node, visited):
    if node not in visited:
        visited.append(node)
        childs = graph[node]
        if len(childs) > 0:
            for child in childs:
                depthFirstTraversalRecursive(graph, child, visited)
    return visited


def depthFirstTraversalIterative(graph, node):
    visited = []
    stack = []
    stack.append(node)
    while len(stack) > 0:
        node = stack[-1]
        if node not in visited:
            visited.append(node)
            childs = graph[node]
            while len(childs) > 0:
                # add the non-visited childs to the stack in reverse order
                child = childs.pop()
                if child not in visited:
                    stack.append(child)
        else:
            stack.pop()
    return visited


def main():
    graph = {'A': ['B', 'C', 'E'],
             'B': ['D', 'F'],
             'C': ['G'],
             'D': [],
             'E': ['F'],
             'F': ['C'],
             'G': []}

    print("Recusrive:")
    result = depthFirstTraversalRecursive(graph, 'A', [])
    for node in result:
        print(node)

    print("Iterative:")
    result2 = depthFirstTraversalIterative(graph, 'A')
    for node in result2:
        print(node)


if __name__ == '__main__':
    main()
