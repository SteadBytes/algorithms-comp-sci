# Recursive Algorithms
To solve a problem, solve a **subproblem** that is a *smaller* instance of the same problem. The use the solution to the smaller instance to solve the original problem.
* Calling same function with smaller parameters = **subproblem**

For computing *n!*, the subproblem is computing *(n-1)!*. Then using the solution for the subproblem to compute *n!*. The **base case** is when *n=0* or *n=1* as these are *always* 1. 

## Rules
* Each recursive call should be on a **smaller instance** of the smae problem
    * A smaller **subproblem**
* Recursive call **must** eventually reach a **base case** which is solved with *no further* recursion.