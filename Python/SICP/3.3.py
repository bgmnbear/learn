# Recursive Data Structures
from numpy.core.umath import square


class Rlist(object):
    """A recursive list consisting of a first element and the rest."""

    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]


s = Rlist(1, Rlist(2, Rlist(3)))
print(s.rest)
print(len(s))
print(s[1])


def extend_rlist(s1, s2):
    if s1 is Rlist.empty:
        return s2
    return Rlist(s1.first, extend_rlist(s1.rest, s2))


print(extend_rlist(s.rest, s))


def map_rlist(s, fn):
    if s is Rlist.empty:
        return s
    return Rlist(fn(s.first), map_rlist(s.rest, fn))


print(map_rlist(s, square))


def filter_rlist(s, fn):
    if s is Rlist.empty:
        return s
    rest = filter_rlist(s.rest, fn)
    if fn(s.first):
        return Rlist(s.first, rest)
    return rest


print(filter_rlist(s, lambda x: x % 2 == 1))


def map_tree(tree, fn):
    if type(tree) != tuple:
        return fn(tree)
    return tuple(map_tree(branch, fn) for branch in tree)


t = ((1, 2), 3, 4)
big_tree = ((t, t), 5)

# print(count_leaves(big_tree))
print(map_tree(big_tree, square))


class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)


def fib_tree(n):
    """Return a Tree that represents a recursive Fibonacci calculation."""
    if n == 1:
        return Tree(0)
    if n == 2:
        return Tree(1)
    left = fib_tree(n - 2)
    right = fib_tree(n - 1)
    return Tree(left.entry + right.entry, left, right)


print(fib_tree(5))

# Set
s = {3, 2, 1, 4, 4}
print(s)

print(3 in s, len(s), s.union({1, 5}), s.intersection({6, 5, 4, 3}))


def empty(s):
    return s is Rlist.empty


def set_contains(s, v):
    """Return True if and only if set s contains v."""
    if empty(s):
        return False
    elif s.first == v:
        return True
    return set_contains(s.rest, v)


s = Rlist(1, Rlist(2, Rlist(3)))
print(set_contains(s, 2))
print(set_contains(s, 5))


def adjoin_set(s, v):
    """Return a set containing all elements of s and element v."""
    if set_contains(s, v):
        return s
    return Rlist(v, s)


t = adjoin_set(s, 4)
print(t)


def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2."""
    set1_not_set2 = filter_rlist(set1, lambda v: not set_contains(set2, v))
    return extend_rlist(set1_not_set2, set2)


print(union_set(t, s))
