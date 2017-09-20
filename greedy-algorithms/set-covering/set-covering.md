# Set-Covering Problem
Given:
* Universe *U* of *n* elements
* Collection of subsets of *U*:
    * *S = {S<sub>1</sub>,S<sub>2</sub>...,S<sub>m</sub>}*
    * Where every substet *S<sub>i</sub>* has an associated cost. 

Find a **minimum cost subcollection** of *S* that covers **all elements of *U***

## NP-Hard Problem
No *polynomial time* optimal solution.
### Optimal Solution
```
Find the power set of S
    Every possible subset of S - 2^n possible subsets
From these, pick the set with the lowest cost that covers all elements of U
```
Takes *O(2<sup>n</sup>)* time to calculate every possible subset of stations.

#### Run time at 10 subsets/second
| Cardinality (size) of *S* | Time Taken to calculate power set |
|:-------------------------:|:---------------------------------:|
| 5                         | 3.2 seconds                       |
| 10                        | 102.4 seconds                     |
| 32                        | 13.6 years                        |
| 100                       |         4x10<sup>21</sup> years         |

## Approximate Greedy Algorithm
```
1. Let I represent set of elements included so far. Initialise I = {}
2. While I != U
    Find set Si in S whose cost effectiveness is smallest. Ratio of Cost(Si) and number of newly added elements is minimum:
        Cost(Si) / |Si - I|
    Add elements of Si to I
```

## Example Uses
### Starting a radio show
Need to reach listeners in all 50 states of America. Must decide which radio stations to play on to reach all states whilst minimising cost of paying to be on each station.
* Minimise number of stations played on.

### Approximate Greedy Solution
```
1. Pick stations that covers the most states that haven't already been covered yet - ok if some states are already covered.
2. Repeat until all states are covered.
```

[Code](radio-stations.py)

### Company needs certain amount of varied supplies. 
Suppliers offer various deals for *different combinations* of materials
* Supplier A: 2000kg of gravel + 1000 bricks for £x. Supplier B: 1000kg os gravel and 4000 bricks for £y etc. 
* Find best way to get all materials whilst minimising cost.
