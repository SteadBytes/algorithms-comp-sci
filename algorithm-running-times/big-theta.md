# Big-&Theta; Notation
*f(n) = &Theta;(g(n))* means that there is an upper and lower bound on *f(n)* for all *n >= n<sub>0</sub>*.
* *c<sub>1</sub> &middot; g(n)* = lower bound on f(n)
* *c<sub>2</sub> &middot; g(n)* = upper bound on f(n)
* There exists constants *c<sub>1</sub>* and *c<sub>2</sub>* such that *f(n) <=c<sub>1</sub> &middot; g(n)* and *f(n) >= c<sub>2</sub> &middot; g(n)*
* *g(n)* therefore gives a **tight bound** on f(n).

    ![](../images/2017-08-29-15-56-57.png)

Once *n* gets large enough (above dotted line on graph above) the running time is **between** *c<sub>1</sub> &middot; g(n)* and *c<sub>2</sub> &middot; g(n)*.

Big-&Theta; notation gives an **asymptotically tight bound** on the running time.
* Asymptotic as only matters for large *n* values.
* Tight bound as the running time is within a constant factor above and below.

Big-&Theta; *automatically* implies both Big-O and Big-&Omega;.
    * Big-O -> upper bound
    * Big-&Omega; -> Lower bound