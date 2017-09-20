from itertools import chain, combinations


def powerset(iterable):
    """Calculate the powerset of any iterable.

    For a range of integers up to the length of the given list,
    make all possible combinations and chain them together as one object.
    From https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    "list(powerset([1,2,3])) --> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def optimal_set_cover(U, S, costs):
    """ Optimal algorithm - DONT USE ON BIG INPUTS - O(2^n)!
    Finds the minimum cost subcollection os S that covers all elements of U

    Args:
        U (list): Universe of elements
        S (dict): Subsets of U {S1:elements,S2:elements}
        costs (dict): Costs of each subset in S - {S1:cost, S2:cost...}
    """
    pset = powerset(S.keys())
    best_set = None
    best_cost = float("inf")
    for subset in pset:
        covered = set()
        cost = 0
        for s in subset:
            covered.update(S[s])
            cost += costs[s]
        if len(covered) == len(U) and cost < best_cost:
            best_set = subset
            best_cost = cost
    return best_set


def greedy_set_cover(universe, subsets, costs):
    """Approximate greedy algorithm for set-covering.
    """
    elements = set(e for s in subsets.keys() for e in subsets[s])
    # elements don't cover universe -> invalid input for set cover
    if elements != universe:
        return None

    # track elements of universe covered
    covered = set()
    cover_sets = []

    while covered != universe:
        min_cost_elem_ratio = float("inf")
        min_set = None
        # find set with minimum cost:elements_added ratio
        for s, elements in subsets.items():
            new_elements = len(elements - covered)
            # set may have same elements as already covered -> new_elements = 0
            # check to avoid division by 0 error
            if new_elements != 0:
                cost_elem_ratio = costs[s] / new_elements
                if cost_elem_ratio < min_cost_elem_ratio:
                    min_cost_elem_ratio = cost_elem_ratio
                    min_set = s
        cover_sets.append(min_set)
        # union
        covered |= subsets[min_set]
    return cover_sets



# U
states = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# S
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
costs = {}
costs['kone'] = 50
costs['ktwo'] = 40
costs['kthree'] = 100
costs['kfour'] = 80
costs['kfive'] = 25

optimal_cover = optimal_set_cover(states, stations, costs)
optimal_cost = sum(costs[s] for s in optimal_cover)

greedy_cover = greedy_set_cover(states, stations, costs)
greedy_cost = sum(costs[s] for s in greedy_cover)

print(optimal_cover)
print(optimal_cost)
print(greedy_cover)
print(greedy_cost)
