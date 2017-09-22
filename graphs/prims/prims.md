# Prims Algorithm
**Greedy** algorithm for Minimum Spanning Tree. Unlike Kruskal's, in all stages of Prim's the current MST is **connected**.

Maintains *two sets* of vertices:
1. Vertices already included in MST
2. Vertices not yet included in MST

At every step a *cut* of the two sets, pick the *minimum weight* edge from the cut and add the vertex to the MST set.

## Algorithm with Priority Queue
**Run time depends**





 on the priority queue implementation.
```Python
def prims(graph, weights):
    #initialise costs[] and parents[]
    for vertex in graph:
        cost[u] = infinity
        parent[u] = None
    # pick any initial node and set cost to 0
    cost[initial_node] = 0

    # priority queue of vertices, using cost-values for priority
    H = PriorityQueue(vertices, priority=costs)

    while H:
        v = deletemin(H)
        for each edge->{v,z}:
            if cost[z] > weights[v,z]:
                cost[z] = weights[v,z]
                parent[z] = v
                decreasekey(H,z)
    return parent
```
## Algorithm without Priority Queue O(|V|<sup>2</sup>)
```python
def prims(graph, weights):
        #initialise costs[] and parents[]
    for vertex in graph:
        cost[u] = infinity
        E[u] = None
    # pick any initial node and set cost to 0
    cost[initial_node] = 0

    mst = set()
    vertices_remaining = set(vertices)

    while vertices_remaining:
        v = minimum cost vertex in vertices_remaining
        mst.add(v)
        if E[v] is not None:
            mst.add(E[v])
        for edge->{v,w}:
            if w in vertices_remaining and weights[v,w] < cost[w]:
                cost[w] = weights[v, w]
                E[w] = [v,w]
    return mst


```
