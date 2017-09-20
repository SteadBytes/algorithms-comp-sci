import unittest


def kruskal(graph):
    """Creates a minimum spanning tree of a graph using kruskals algorithm.

    Args:
        graph (dict): weighted graph structure in form 
            `{node1:{adjacent_node:weight,...}, node2:{...}...}
    Returns: tuple (mst, total_weight)
        mst (set): Set of tuples (v, u) representing edges in MST
        total_weight (number): total weight of MST
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

    # list of tuples of edge components : [(v,u), ...]
    sorted_edges = sorted(edges.keys(), key=lambda edge: edges[edge])

    for edge in sorted_edges:
        v, u = edge
        # find returns the set vertex belongs to
        if find(v, parents) != find(u, parents):
            mst.add((v, u))
            union(v, u, parents, ranks)  # merge sets containing u, v

    total_weight = sum(edges[x] for x in mst)
    return mst, total_weight


def makeset(x, parents, ranks):
    """Creates a new tree representing a set of a single element.

    Args:
        x : Key/name of vertex to create set with
        parents (dict): Node->parent pointers 
                        e.g. {node1:parent,node2:parent...}
        ranks (dict): Node ranks = height of subtree rooted at each node:
                        e.g. {node1: rank,node2: rank}
    """
    parents[x] = x
    ranks[x] = 0


def find(x, parents):
    """Finds the representative/root node of an element in a set.

    Args:
        x : Key/name of vertex to find parent of
        parents (dict): Node->parent pointers 
                        e.g. {node1:parent,node2:parent...}
    Returns:
        key/name of representative/root node
    """
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]


def union(x, y, parents, ranks):
    """Merge sets using Union by Rank.

    Args:
        x : Key/name of a vertex in first set
        y : Key/name of a vertex in second set 
        parents (dict): Node->parent pointers 
                        e.g. {node1:parent,node2:parent...}
        ranks (dict): Node ranks = height of subtree rooted at each node:
                        e.g. {node1: rank,node2: rank}      
    """
    # get root nodes of each tree
    root_x = find(x, parents)
    root_y = find(y, parents)

    # trees already merged
    if root_x == root_y:
        return
    # merge smaller tree into bigger tree
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y
        # increase height of merged tree when each tree is equal height
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] = ranks[root_y] + 1


class KruskalsMSTTest(unittest.TestCase):
    def setUp(self):
        self.graph = {"A": {"B": 25, "C": 35},
                      "B": {"C": 15, "E": 90},
                      "C": {"B": 50, "D": 50, "E": 30},
                      "D": {"E": 60, "F": 20},
                      "E": {"D": 10, "F": 70},
                      "F": {}
                      }

    def test_MST_correct(self):
        """Check that kruskals produces correct 
        """
        mst_expected = {('E', 'D'), ('B', 'C'), ('D', 'F'),
                        ('C', 'E'), ('A', 'B')}
        for e, f in zip(kruskal(self.graph)[0], mst_expected):
            self.assertEqual(min(e), min(f))
            self.assertEqual(max(e), max(f))

    def test_MST_all_vertices(self):
        """Each vertex should appear in MST either 1 or two times

        Most vertices are both a start of edge and end of edge -> 2 times
        First and last vertices appear only 1 time 
        """
        mst = kruskal(self.graph)[0]
        flattened = [item for templist in mst for item in templist]
        for vertex in self.graph.keys():
            count = flattened.count(vertex)
            self.assertTrue(count > 0 and count <= 2)


if __name__ == "__main__":
    unittest.main()
