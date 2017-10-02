'''

Depth First Traversal implementation using the stack concept

Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges
'''


def dft(vertex, graph):
    '''
    :param vertex: an element(text or number) representing a vertex
    :param graph: dictionary where a key if a vertex and their values the adjacent vertices

    '''
    stack = list()
    return dft_recursive(vertex, graph, stack)


def dft_recursive(vertex, graph, stack):
    '''
    :param stack: Stack where we put the next vertices to visit

    '''
    stack.append(vertex)
    vertices = graph.get(vertex)
    if vertices is not None:
        for v in vertices:
            if v not in stack:
                dft_recursive(v, graph, stack)
    return stack


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
    result = dft('a', graph)
    result_to_text = ""
    for element in result:
        result_to_text = result_to_text + element
        if element != result[-1]:
            result_to_text += " -> "

    print(result_to_text)


if __name__ == '__main__':
    main()
