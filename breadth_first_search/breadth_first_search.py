"""
Breadth-first search (BFS) is an algorithm for searching tree or
graph data structures. It produces a set of actions to be follwed to reach a
target state from the start state. Starting at the initial state (often the
root node for a tree) it explores all neighbor nodes at each level
before moving to the next level.
"""

from collections import deque, namedtuple


def breadth_first_search(graph, start, target):
    """ Performs a breadth-first search on a graph

    Args:
        graph (list of list of int): Adjacency matrix representation of graph
        source (int): Index of source vertex to begin search from

    Returns:
        tuple (path, distance): path traversed from start to target, total
            distance of path
        None,None if target not found
    """
    vertex_info = {}
    VistitedVertex = namedtuple("VisitedVertex", "parent distance")
    vertex_info[start] = VistitedVertex(None, 0)

    search_queue = deque()
    visited = set()
    search_queue.append(start)

    while search_queue:
        u = search_queue.popleft()
        if u == target:
            return construct_path(u, vertex_info)
        for v in graph[u]:
            if v not in visited:
                if v not in search_queue:
                    vertex_info[v] = VistitedVertex(
                        u, vertex_info[u].distance + 1)
                    search_queue.append(v)
        visited.add(u)
    return None, None


def construct_path(vertex, vertex_info):
    path = []
    distance = vertex_info[vertex].distance
    while True:
        path.append(vertex)
        if vertex_info[vertex].parent is not None:
            vertex = vertex_info[vertex].parent
        else:
            break
    return path[::-1], distance


def main():
    graph_adj_list = [
        [1],
        [0, 4, 5],
        [3, 4, 5],
        [2, 6],
        [1, 2],
        [1, 2, 6],
        [3, 5],
        []
    ]

    start = 0
    target = 10
    path, distance = breadth_first_search(graph_adj_list, start, target)
    print('Path from vertex {} to vertex {}: {}'.format(start, target, path))
    print('Path distance: {}'.format(distance))


if __name__ == '__main__':
    main()
