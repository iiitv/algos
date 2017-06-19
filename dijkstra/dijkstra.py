"""
Dijktra's shortest path algorithm. Finds the path and distance from source to target.
To add an edge between vertex a and b with distance dist:
    graph[a].append((b, dist)) and graph[b].append((a, dist)).
"""


import heapq


def dijkstra(graph, source, target):
    """
    Finds the shortest path and shortest distance from source to target

    :param graph: Dictionary linking the vertices using list of tuples
    :param source: The vertex to start the path.
    :param target: The vertex to end the path.
    :return: shortest path and distance from source to target
    """
    INF = float('Inf')
    predecessors = {x: x for x in graph}
    distances = {x: INF for x in graph}
    distances[source] = 0
    temp = []
    heapq.heappush(temp, [source, distances[source]])

    while temp:
        u = heapq.heappop(temp)
        u_dist = u[1]
        u_idx = u[0]
        if u_dist == distances[u_idx]:
            for v in graph[u_idx]:
                v_idx = v[0]
                u2v = v[1]
                if distances[u_idx] + u2v < distances[v_idx]:
                    distances[v_idx] = distances[u_idx] + u2v
                    heapq.heappush(temp, [v_idx, distances[v_idx]])
                    predecessors[v_idx] = u_idx

    if distances[target] == INF:
        return None, None
    else:
        path = []
        vertex = target
        while True:
            path.append(str(vertex))
            if vertex == predecessors[vertex]:
                break
            vertex = predecessors[vertex]
        return path[::-1], distances[target]


def main():
    """
    driver function to test the dijkstra's algorithm
    """
    graph = {'s': [('a', 2), ('b', 1)],
             'a': [('s', 3), ('b', 4), ('c', 8)],
             'b': [('s', 4), ('a', 2), ('d', 2)],
             'c': [('a', 2), ('d', 7), ('t', 4)],
             'd': [('b', 1), ('c', 11), ('t', 5)],
             't': [('c', 3), ('d', 5)]
             }
    source = 'a'
    target = 't'
    path, cost = dijkstra(graph, source, target)
    print('The path from ' + source + ' to ' + target + ' :')
    if path is None or cost is None:
        print('does not exist')
    else:
        print(str(path) + ' with cost: ' + str(cost))


if __name__ == "__main__":
    main()
