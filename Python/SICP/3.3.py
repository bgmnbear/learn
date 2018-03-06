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
