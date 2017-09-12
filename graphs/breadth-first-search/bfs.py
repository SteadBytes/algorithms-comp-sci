from collections import deque


def bfs(graph, source):
    """ Performs a breadth-first search on a graph

    Args:
        graph (list of list of int): Adjacency matrix representation of graph
        source (int): Index of source vertex to begin search from

    Returns:
        list of dicts describing each vertex -> [{distance: _, predecessor: _ }] 
    """
    vertexInfo = []
    for i in range(len(graph)):
        vertexInfo.append({"distance": None, "predecessor": None})
    vertexInfo[source]["distance"] = 0

    search_queue = deque()
    search_queue.append(source)

    while search_queue:
        u = search_queue.popleft()
        for v in graph[u]:
            if vertexInfo[v]["distance"] is None:
                vertexInfo[v]["distance"] = vertexInfo[u]["distance"] + 1
                vertexInfo[v]["predecessor"] = u
                search_queue.append(v)
    return vertexInfo


# Testing --------------------

adjList = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
]

vertexInfo = bfs(adjList, 3)

for i in range(len(adjList)):
    print("vertex %s : distance = %s, predecessor = %s" %
          (i, vertexInfo[i]["distance"], vertexInfo[i]["predecessor"]));

assert(vertexInfo[0] == {
    "distance": 4,
    "predecessor": 1
});
assert(vertexInfo[1] == {
    "distance": 3,
    "predecessor": 4
});
assert(vertexInfo[2] == {
    "distance": 1,
    "predecessor": 3
});
assert(vertexInfo[3] == {
    "distance": 0,
    "predecessor": None
});
assert(vertexInfo[4] == {
    "distance": 2,
    "predecessor": 2
});
assert(vertexInfo[5] == {
    "distance": 2,
    "predecessor": 2
});
assert(vertexInfo[6] == {
    "distance": 1,
    "predecessor": 3
});
assert(vertexInfo[7] == {
    "distance": None,
    "predecessor": None
});
