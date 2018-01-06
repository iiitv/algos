"""
Breadth-first-traversal is an algorithm for traversing a tree or
graph data structure. Starting at the tree root (or some arbitrary node of a
graph, sometimes referred to as a 'search key'[1]) and explores the neighbor
nodes at that level first, before moving to the next level.
"""

from collections import deque


def breadth_first_traversal(graph, source):
    """ Performs a breadth-first traversal on a graph

    Args:
        graph (list of list of int): Adjacency matrix representation of graph
        source (int): Index of source vertex to begin search from

    Returns:
        list of dicts describing each vertex in the searched graph
            -> [{distance: _, predecessor: _ }]
    """
    vertex_info = []
    for i in range(len(graph)):
        vertex_info.append({"distance": None, "predecessor": None})
    vertex_info[source]["distance"] = 0

    search_queue = deque()
    search_queue.append(source)

    while search_queue:
        u = search_queue.popleft()
        for v in graph[u]:
            if vertex_info[v]["distance"] is None:
                vertex_info[v]["distance"] = vertex_info[u]["distance"] + 1
                vertex_info[v]["predecessor"] = u
                search_queue.append(v)
    return vertex_info


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
    vertex_info = breadth_first_traversal(graph_adj_list, 3)

    for i in range(len(graph_adj_list)):
        print("vertex %s : distance = %s, predecessor = %s" %
              (i, vertex_info[i]["distance"], vertex_info[i]["predecessor"]))

    assert(vertex_info[0] == {
        "distance": 4,
        "predecessor": 1
    })
    assert(vertex_info[1] == {
        "distance": 3,
        "predecessor": 4
    })
    assert(vertex_info[2] == {
        "distance": 1,
        "predecessor": 3
    })
    assert(vertex_info[3] == {
        "distance": 0,
        "predecessor": None
    })
    assert(vertex_info[4] == {
        "distance": 2,
        "predecessor": 2
    })
    assert(vertex_info[5] == {
        "distance": 2,
        "predecessor": 2
    })
    assert(vertex_info[6] == {
        "distance": 1,
        "predecessor": 3
    })
    assert(vertex_info[7] == {
        "distance": None,
        "predecessor": None
    })


if __name__ == '__main__':
    main()
