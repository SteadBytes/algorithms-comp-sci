from math import factorial


def bernoulli_fast(n):
    """ Calculates all Bernoulli numbers up to n using the Akiyama-Tanigawa
    algorithm
    """
    res = []
    values = []
    for m in range(0, n + 1):
        values.append(1 / (m + 1))
        for j in range(m, 0, -1):
            values[j - 1] -= values[j]
            values[j - 1] *= j
        res.append(values[0])
    return res


def combination(n, k):
    if k <= n:
        return (factorial(n) / (factorial(k) * factorial(n - k)))
    else:
        return 0


def bernoulli_recurisive(m):
    if m == 0:
        return 1
    else:
        tmp = 0
        for k in range(m):
            tmp += combination(m, k) * bernoulli_recurisive(k) / (m - k + 1)
    return 1 - tmp
