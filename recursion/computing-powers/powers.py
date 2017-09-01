def isEven(n):
    return n % 2 == 0


def isOdd(n):
    return not isEven(n)


def power(x, n):
    """Computes x to the power of n

    Args:
        x (number):  Base
        n (int): Exponent
    Returns:
        (number) x^n
    """
    # base case
    if n == 0:
        return 1

    # n = negative
    # MUST COME BEFORE ODD/EVEN CHECKS
    # isOdd/Even will return True for negatives
    # Exponent wont get smaller -> won't terminate
    if(n < 0):
        return 1 / power(x, -n)
    # n = positive and odd
    if(isOdd(n)):
        return x * power(x, n - 1)

    # n = positive and even
    if (isEven(n)):
        y = power(x, n / 2)
        return y * y


def display_power(x, n):
    print("%s^%s = %s" % (x, n, power(x, n)))


display_power(3, 0)
assert(power(3, 0) == 1)

display_power(-3, 0)
assert(power(-3, 0) == 1)

display_power(3, 1)
assert(power(3, 1) == 3)

display_power(3, 2)
assert(power(3, 2) == 9)

display_power(3, 3)
assert(power(3, 3) == 27)

display_power(3, -2)
assert(power(3, -2) == 1 / 9)


display_power(-3, -2)
assert(power(-3, -2) == 1 / 9)
