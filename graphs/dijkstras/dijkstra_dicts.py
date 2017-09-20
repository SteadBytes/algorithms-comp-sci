def dijkstra(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    # stop when all nodes processed
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node



# Starting from node A to F
graph = {"A": {"B": 25, "C": 35},
         "B": {"C": 15, "E": 90},
         "C": {"B": 50, "D": 50, "E": 30},
         "D": {"E": 60, "F": 20},
         "E": {"D": 10, "F": 70},
         "F": {}
         }
inf = float("inf")  # python infinity
costs = {"A": 0, "B": 25, "C": 35, "D": inf, "E": inf, "F": inf}
parents = {"A": None, "B": "A", "C": "A", "D": None, "E": None, "F": None}
print("Before dijkstra:")
print("Costs: %s" % costs)
print("Parents: %s" % parents)
dijkstra(graph, costs, parents)
print("After dijkstra:")
print("Costs: %s" % costs)
print("Parents: %s" % parents)
