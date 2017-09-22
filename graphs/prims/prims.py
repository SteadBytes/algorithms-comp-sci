import unittest


def prims(graph):
    """Creates a minimum spanning tree of a graph using Prim's algorithm


    Args:
        graph (dict): weighted graph structure in form
            `{node1:{adjacent_node:weight,...}, node2:{...}...}
    Returns:
        (dict): MST in vertex->parent form - {vertex:parent,...}
    """
    vertices = list(graph.keys())
    costs = dict.fromkeys(vertices, float("inf"))
    parents = dict.fromkeys(vertices, None)

    # any initial node
    costs[vertices[0]] = 0

    mst = set()
    vertices_remaining = set(vertices)

    while vertices_remaining:
        v = min(vertices_remaining, key=costs.get)
        vertices_remaining.remove(v)
        mst.add(v)
        if parents[v] is not None:
            mst.add(parents[v])
        for u, weight in graph[v].items():
            if u in vertices_remaining and weight < costs[u]:
                costs[u] = weight
                parents[u] = v
    return parents


def mst_to_edges(mst):
    """Creates a list of edges from mst vertex->parent

    Args:
        mst (dict): MST in vertex->parent form - {vertex:parent,...}
    Returns:
        (list of tuple): Edges in form (v, u)
    """
    return [(parent, vertex) for vertex, parent in mst.items() if parent]


def graph_weight(edges, graph):
    """Calculates the total weight of a given list of edges in a graph.

    Args:
        edges (list of tuple): Edges in form (v, u)
        graph (dict): weighted graph structure in form
            `{node1:{adjacent_node:weight,...}, node2:{...}...}
    Returns:
        (int): total weight of the graph
    """
    return sum([graph[edge[0]][edge[1]] for edge in edges])

# Examples:
# graph = {"A": {"B": 25, "C": 35},
#          "B": {"C": 15, "E": 90},
#          "C": {"B": 50, "D": 50, "E": 30},
#          "D": {"E": 60, "F": 20},
#          "E": {"D": 10, "F": 70},
#          "F": {}
#          }

# mst_parents = prims(graph)
# mst_edges = mst_to_edges(mst_parents)
# weight = graph_weight(mst_edges, graph)
# print(mst_parents)
# print(mst_edges)
# print(weight)


class PrimsMSTTests(unittest.TestCase):
    def setUp(self):
        self.graph = {"A": {"B": 25, "C": 35},
                      "B": {"C": 15, "E": 90},
                      "C": {"B": 50, "D": 50, "E": 30},
                      "D": {"E": 60, "F": 20},
                      "E": {"D": 10, "F": 70},
                      "F": {}
                      }

    def test_MST_correct(self):
        """Test whether prims produces correct MST
        """
        mst_edges_expected = [('A', 'B'), ('B', 'C'), ('E', 'D'),
                              ('C', 'E'), ('D', 'F')]
        mst_parents = prims(self.graph)
        for e, f in zip(mst_to_edges(mst_parents), mst_edges_expected):
            # min/max comparisons will work for str and int values
            self.assertEqual(min(e), min(f))
            self.assertEqual(max(e), max(f))

    def test_MST_all_vertices(self):
        """Each vertex should appear in MST either 1 or two times

      Most vertices are both a start of edge and end of edge -> 2 times
      First and last vertices appear only 1 time 
      """
        mst_parents = prims(self.graph)
        mst_edges = mst_to_edges(mst_parents)
        flattened = [item for templist in mst_edges for item in templist]
        for vertex in self.graph.keys():
            count = flattened.count(vertex)
            self.assertTrue(count > 0 and count <= 2)


if __name__ == '__main__':
    unittest.main()
