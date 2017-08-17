'''

BreadthFirstSearch implementation using the queue concept
Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges
'''


def bfs(vertex, graph):
    '''
    :param vertex: an element (text or number) representing a vertex
    :param graph: dictionary where a key if a vertex and their values the adjacent vertices

    '''
    queue = list()
    path = list()
    queue.insert(0, vertex)
    return bfs_recursive(vertex, graph, queue, path)


def bfs_recursive(vertex, graph, queue, path):
    '''
    :param queue: queue where we put the next vertex to search on
    :param path: the list containing the elements belonging to the search
    :return:
    '''
    if vertex not in path:
        path.append(vertex)
        queue.pop(0)
        vertices = graph.get(vertex)
        if vertices is not None:
            queue = queue + vertices
            queue = [v for v in queue if v not in path]
    if queue == []:
        return path
    else:
        return bfs_recursive(queue[0], graph, queue, path)


def main():
    graph = {
        'a': ['c', 'd', 'h'],
        'b': ['h'],
        'c': ['a', 'g'],
        'd': ['a', 'e', 'f'],
        'e': ['d', 'f', 'g', 'h'],
        'f': ['d', 'e'],
        'g': ['c', 'e'],
        'h': ['a', 'b', 'e']
    }

    result = bfs('a', graph)
    result_to_text = ""
    for element in result:
        result_to_text = result_to_text + element
        if element != result[-1]:
            result_to_text += " -> "

    print(result_to_text)


if __name__ == '__main__':
    main()
