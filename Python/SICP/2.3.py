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
