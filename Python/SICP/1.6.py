# Function as a parameter
def summation(n, term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total


def cube(k):
    return pow(k, 3)


def successor(k):
    return k + 1


def sum_cubes(n):
    return summation(n, cube, successor)


#
def identity(k):
    return k


def sum_naturals(n):
    return summation(n, identity, successor)


# As a general method of function
def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess


def near(x, f, g):
    return approx_eq(f(x), g(x))


def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


def golden_update(guess):
    return 1 / guess + 1


def square(x):
    return x * x


def golden_test(guess):
    return near(guess, square, successor)


print('Golden ratio', iter_improve(golden_update, golden_test))


# Nested definition
def average(x, y):
    return (x + y) / 2


def square_root(x):
    def update(guess):
        return average(guess, x / guess)

    def test(guess):
        return approx_eq(square(guess), x)

    return iter_improve(update, test)


print('squrare root', square_root(256))


# As a function of the return value
def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


add_one_and_square = compose1(square, successor)
print('add_one_and_square', add_one_and_square(12))


# Lambda expression
def compose1(f, g):
    return lambda x: f(g(x))


# Function decorator
def trace1(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)

    return wrapped


@trace1
def triple(x):
    return 3 * x


triple(12)
