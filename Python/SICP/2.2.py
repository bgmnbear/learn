# Data abstraction
from operator import getitem
from fractions import gcd


def make_rat(n, d):
    g = gcd(n, d)
    return (n // g, d // g)


def numer(x):
    return getitem(x, 0)


def denom(x):
    return getitem(x, 1)


def add_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx * dy + ny * dx, dx * dy)


def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def eq_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def str_rat(x):
    """Return a string 'n/d' for numerator n and denominator d."""
    return '{0}/{1}'.format(numer(x), denom(x))


half = make_rat(1, 2)
print(str_rat(half))

third = make_rat(1, 3)
print(str_rat(mul_rat(half, third)))

print(str_rat(add_rat(third, third)))


# Data attributes
def make_pair(x, y):
    """Return a function that behaves like a pair."""

    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y

    return dispatch


def getitem_pair(p, i):
    """Return the element at index i of pair p."""
    return p(i)


p = make_pair(1, 2)
print(getitem_pair(p, 0))
print(getitem_pair(p, 1))
