graph = {"A": {"B": 25, "C": 35},
         "B": {"C": 15, "E": 90},
         "C": {"B": 50, "D": 50, "E": 30},
         "D": {"E": 60, "F": 20},
         "E": {"D": 10, "F": 70},
         "F": {}
         }


def kruskal(graph):
    """Creates a minimum spanning tree of a graph using kruskals algorithm.

    Args:
        graph (dict): weighted graph structure in form 
            `{node1:{adjacent_node:weight,...}, node2:{...}...}
    Returns:
        (set): Set of tuples (v, u) representing edges in mst
    """
    parents = dict.fromkeys(graph)
    ranks = dict.fromkeys(graph)

    for vertex in graph.keys():
        makeset(vertex, parents, ranks)

    mst = set()  # Current spanning tree
    edges = dict()  # edges with corresponding weights

    for v in graph.keys():
        for u in graph[v].keys():
            edges[(v, u)] = graph[v][u]

    # list of tuples : [((u,v), weight), ...]
    # TODO: Does this need to include weights?? Just be keys
    # then access edges dict for weights?
    sorted_edges = sorted(edges.items(), key=lambda value: value[1])

    for edge in sorted_edges:
        v, u = edge[0]
        if find(v, parents) != find(u, parents):  # find returns the set vertex belongs to
            mst.add((v, u))
            union(v, u, parents, ranks)  # merge sets containing u, v

    mst_weight = sum(edges[x] for x in mst)

    print(mst_weight)

    return mst


def makeset(x, parents, ranks):
    parents[x] = x
    ranks[x] = 0


def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]


def union(x, y, parents, ranks):
    root_x = find(x, parents)
    root_y = find(y, parents)

    if root_x == root_y:
        return
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] = ranks[root_y] + 1


print(kruskal(graph))
