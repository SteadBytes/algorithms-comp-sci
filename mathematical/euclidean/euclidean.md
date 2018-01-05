# Euclidean Algorithm
Technique for quickly finding the greatest common divisor (GCD) of two integers
* GCD of two integers A and B = largest integer that divides both A and B

Uses properties:
* GCD(A,0) = A
* GCD(0,B) = B
* If A=B&middot;Q and B!=0 then GCD(A,B)=GCD(B,R)
    * Where Q is an integer and R is an integer between 0 and B-1

## Algorithm
GCD(A,B):
* If A=0 then GCD(A,B)=B, Stop
    * Since GCD(0,B) = B
* If B=0 then GCD(A,B)=A, Stop
    * Since GCD(A,0) = A
* Write A in quotient remainder form: A=B&middot;Q + R
* Find GCD(B,R) using Euclidean Algorithm
    * Since GCD(A,B) = GCD(B,R)
```Python 
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    r = a%b
    return gcd(b,r)
```