# Extended Euclidean Algorithm
Computes the GCD and coefficients *x* and *y* of two integers *a* and *b* such that:
* *ax* + *by* = gcd(*a*,*b*)
    *   Bézout's identity

When *a* and *b* are **coprime**, *x* = **modular multiplicative inverse of *a* modulo *b***

## Algorithm
The GCD of two positive integers *a* and *b* can be equated to a **Linear Combination** of *a* and *b*:
* gcd(*a*,*b*) = *ax* + *by* 
Example, *a* = 1180, *b* = 482:
1. Calculate gcd(1180, 482):
    1. 1180 = 482(2) + 216
    2. 482 = 216(2) + 50
    3. 216 = 50(4) + 16
    4. 50 = 16(3) + 2
    5. 16 = 2(8) + 0 -> remainder = 0 -> stop
    6. gcd = 2
2. Work backwards from the end of step 1. to produce a linear equation for gcd(1180, 482) = 2 in the form 2 = 1180x + 482y:
    1. 2 = 50 + 16(-3)
        * From 1.4
    2. 2 = 50 + (216+50(-4))(-3)
        * From 1.3
    3. 2 = 216(-3) + 50(13)
    4. 2 = 216(-3) + (482+216(-2))
        * From 1.2
    5. 2 = 216(-29) + 482(13)
    6. 2 = (1180+482(-2))(-29) + 482(13)
        * From 1.1
    7. 2 = 1180(-29) + 482(71)
    8. ANSWER: x = -29, y = 71


```Python
def extended_gcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r !=0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    print('Bezout Coeff: %s, %s'%(old_s, old_t))
    print('GCD: %s'% old_r)
    print('Quotients by the GCD: %s, %s'%(t, s))
```