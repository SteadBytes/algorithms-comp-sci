# Greedy Algorithms
At each step, the **locally optimal** solution is chosen in order to build the *globally* optimal solution **at the end**.

Optimal solutions to some problems can be intractable or not worth the complexity of the algorithm required to find them. Greedy algorithms work well here because they are **simple and get 'pretty close'** ,*but not quite*, to the optimal solution. 

## Examples
* [Prim's](../graphs/prims/prims.md) algorithm and [Kruskal's](../graphs/kruskals/kruskals.md) algorithm
    * Finding minimum spanning trees
* [Dijkstra's](../graphs/dijkstras/dijkstras.md
) algorithm
    * Optimal path finding in a graph
* Huffman Encoding
* Set-Covering Problem
* Knapsack Problem

## Approximation Algorithms
Provide a solution to a problem that is **provably close** to optimal. Used when the optimal solution is intractable or when a near-optimal solution can be found quickly and an exact solution is not needed.

Quality is determined by:
* Speed of algorihtm
* Closeness to optimal solution - approximation ratio.
    * Ratio between result obtained and the optimal cost.
    * Algorithm that solves for £2 an instance of a problem that has an optimal of £1 has approcimation ratio of 2.

Greedy algorithms work well as they are simple to produce and ,usually, run fast.

## Knapsack Problem
Knapsack has maximum weight it can hold. Have to fill knapsack with items - maximizing total value.
* Pick the highest value item that will fit
* Pick the next highest value item that will fit in remaining space
* Repeat until no items can fit into knapsack.

*Does not* give optimal solution, but is an easily computable algorithm to get 'pretty close'.