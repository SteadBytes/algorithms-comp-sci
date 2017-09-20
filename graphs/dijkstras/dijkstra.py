from collections import deque


def dijkstra(graph, source):
    """ Runs dijkstras algorithm on a weighted graph to create optimal paths
    between nodes

    Args:
        graph (dict) - Graph in the form `{node1 : {neighbour1 : weight, 
        neighbour2 : weight}, node2 :{} ...}`

        source - key of the source node in graph

    Returns:
        **tuple** - (dist, parents):
        - dist (dict) : Distances from source to each node
        - parents (dict): Proceeding node of each node in the optimal path
    """
    S = set()  # track processed nodes
    Q = deque(graph.keys())  # nodes retrieved from -> empty at end

    # distances from source to each node in graph
    dist = dict.fromkeys(graph, float("inf"))
    dist[source] = 0

    parents = dict.fromkeys(graph, None)

    while Q:
        # minimum distance node not yet processed
        v = min((set(dist.keys()) - S), key=dist.get)
        Q.remove(v)
        S.add(v)
        for u in graph[v].keys():
            if u in Q:
                alt = dist[v] + graph[v][u]
                if alt < dist[u]:
                    dist[u] = alt
                    parents[u] = v
    return dist, parents


def optimal_path(graph, source, target):
    """ Uses dijkstras algorithm to find the optimal path between two nodes
    in a weighted graph

    Args:
        graph (dict) - Graph in the form `{node1 : {neighbour1 : weight, 
        neighbour2 : weight}, node2 :{} ...}`

        source - key of the source node in graph
        target - key of the target node in graph
    Returns: **tuple** (path, weight)
        - path - array of nodes giving the optimal path
        - weight - measure of weight for the optimal path
    """
    dist, parents = dijkstra(graph, source)

    path = []
    v = target
    while v is not None:
        path.append(v)
        v = parents[v]

    path.reverse()

    return path, dist[target]


graph = {"A": {"B": 25, "C": 35},
         "B": {"C": 15, "E": 90},
         "C": {"B": 50, "D": 50, "E": 30},
         "D": {"E": 60, "F": 20},
         "E": {"D": 10, "F": 70},
         "F": {}
         }

print(optimal_path(graph, "A", "E"))
