# sequence

# Even pair
print(((1, 2), (3, 4)))

# Recursive list
empty_rlist = None


def make_rlist(first, rest):
    """Make a recursive list from its first element and the rest."""
    return (first, rest)


def first(s):
    """Return the first element of a recursive list s."""
    return s[0]


def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]


counts = make_rlist(1, make_rlist(2, make_rlist(3, make_rlist(4, empty_rlist))))

print(first(counts))
print(rest(counts))


def len_rlist(s):
    """Return the length of recursive list s."""
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length


def getitem_rlist(s, i):
    """Return the element at index i of recursive list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


print(len_rlist(counts))
print(getitem_rlist(counts, 1))

# tuple
digits = (1, 8, 2, 8)
print(len(digits))
print(digits[3])

print((2, 7) + digits * 2)

alternates = (-1, 2, -3, 4, -5)
print(tuple(map(abs, alternates)))


# Sequence iteration
def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total


print(count(digits, 8))

pairs = ((1, 2), (2, 2), (2, 3), (4, 4))

same_count = 0
for x, y in pairs:
    if x == y:
        same_count = same_count + 1

print(same_count)

print(tuple(range(5, 8)))

for _ in range(3):
    print('Go Bears!')


# String

# Interface conventions
def fib(k):
    """Compute the kth Fibonacci number."""
    prev, curr = 1, 0  # curr is the first Fibonacci number.
    for _ in range(k - 1):
        prev, curr = curr, prev + curr
    return curr


def iseven(n):
    return n % 2 == 0


def sum_even_fibs(n):
    """Sum the first n even Fibonacci numbers."""
    return sum(filter(iseven, map(fib, range(1, n + 1))))


print(sum_even_fibs(20))


def first(s):
    return s[0]


def iscap(s):
    return len(s) > 0 and s[0].isupper()


def acronym(name):
    """Return a tuple of the letters that form the acronym for name."""
    return tuple(map(first, filter(iscap, name.split())))


print(acronym('University of California Berkeley Undergraduate Graphics Group'))


def acronym(name):
    return tuple(w[0] for w in name.split() if iscap(w))


def sum_even_fibs(n):
    return sum(fib(k) for k in range(1, n + 1) if fib(k) % 2 == 0)


from operator import mul
from functools import reduce

print(reduce(mul, (1, 2, 3, 4, 5)))


def product_even_fibs(n):
    """Return the product of the first n even Fibonacci numbers, except 0."""
    return reduce(mul, filter(iseven, map(fib, range(2, n + 1))))


print(product_even_fibs(20))
