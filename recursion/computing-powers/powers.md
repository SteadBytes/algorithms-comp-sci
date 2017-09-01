# Computing Powers of a Number
*x<sup>0</sup> = 0* -> **Base Case**

Exponent Product Rule:
* *x<sup>a</sup> &middot; x<sup>b</sup> = x<sup>a+b</sup>*

If *n* is positive and even, *x<sup>n</sup> = x<sup>n/2</sup> &middot; x<sup>n/2</sup>*
* Where *n* is positive *and* even

Computing *y=x<sup>n/2</sup>* recursively gives *x<sup>n</sup>=y &middot; y*.

If *n* is positive and **odd**, *x<sup>n</sup> = x<sup>n-1</sup> &middot; x*
* *x<sup>n-1</sup> &middot; x = x<sup>n-1</sup> &middot; x<sup>1</sup> = x<sup>(n-1)+1</sup>*
* *n-1* will be **either 0 or positive and even**.
    * *x<sup>0</sup>* = 1 -> Base case
    * Positve and even exponent -> recursive rule above.
    * Therefore compute *x<sup>n-1</sup>* recursively to compute *x<sup>n</sup> = x<sup>n-1</sup> &middot; x*

Reciprocal Rule:
* *x<sup>n</sup> = 1/x<sup>-n</sup>*

If *n* is negative, use the reciprocal rule to compute *x<sup>-n</sup>* recursively and take it's **reciprocal**
* Since *n* is negative, *-n* is positive -> use positive rule above.

## Recursive Algorithm
* Base Case:
    *  *n = 0, x<sup>0</sup>=1* -> 
* *n* is positive and even:
    * Recursively compute *y=x<sup>n/2</sup>* and then *x<sup>n</sup>=y &middot; y*.
    * Use **one** recursive call then multiply result by itself.
* *n* is positive and odd:
    * Recursively compute *x<sup>n-1</sup>*
        * Exponent is either 0 or positive and even
    * Then compute *x<sup>n-1</sup> &middot; x*
* *n* is negative:
    * Recursively compute *x<sup>-n</sup>*
        * Exponent becomes positive
    * Then compute *x<sup>n</sup> = 1/x<sup>-n</sup>*

```Javascript
function power (x, n) {
    console.log("Computing " + x + " raised to power " + n + ".");
    // base case
    if (n===0){
        return 1;
    }
    // recursive case: n is negative
    if(n < 0){
        return 1/power(x,-n);
    }
    // recursive case: n is odd
    if(isOdd(n)){
        return x * power(x, n-1);
    }
    // recursive case: n is even
    if(isEven(n)){
        var y = power(x, n/2);
        return y*y;
    }
};
```