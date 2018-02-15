# Variable data

# Local status
def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""

    def withdraw(amount):
        nonlocal balance  # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount  # Re-bind the existing balance name
        return balance

    return withdraw


wd = make_withdraw(20)
print(wd(5))
print(wd(3))

wd2 = make_withdraw(7)
print(wd2(6))

wd = make_withdraw(12)
wd2 = wd
print(wd2(1))
print(wd(1))

# List
chinese_suits = ['coin', 'string', 'myriad']
suits = chinese_suits
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
print(suits)
suits[0:2] = ['heart', 'diamond']
print(suits)

nest = list(suits)
nest[0] = suits
suits.insert(2, 'Joker')
print(nest)

# def make_mutable_rlist():
#     """Return a functional implementation of a mutable recursive list."""
#     contents = empty_rlist
#
#     def dispatch(message, value=None):
#         nonlocal contents
#         if message == 'len':
#             return len_rlist(contents)
#         elif message == 'getitem':
#             return getitem_rlist(contents, value)
#         elif message == 'push_first':
#             contents = make_rlist(value, contents)
#         elif message == 'pop_first':
#             f = first(contents)
#             contents = rest(contents)
#             return f
#         elif message == 'str':
#             return str(contents)
#
#     return dispatch


# def to_mutable_rlist(source):
#     """Return a functional list with the same contents as source."""
#     s = make_mutable_rlist()
#     for element in reversed(source):
#         s('push_first', element)
#     return s


# Dict
print(dict([(3, 9), (4, 16), (5, 25)]))


def make_dict():
    """Return a functional implementation of a dictionary."""
    records = []

    def getitem(key):
        for k, v in records:
            if k == key:
                return v

    def setitem(key, value):
        for item in records:
            if item[0] == key:
                item[1] = value
                return
        records.append([key, value])

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
        elif message == 'keys':
            return tuple(k for k, _ in records)
        elif message == 'values':
            return tuple(v for _, v in records)

    return dispatch


d = make_dict()
d('setitem', 3, 9)
d('setitem', 4, 16)

print(d('getitem', 3))
print(d('getitem', 4))
print(d('keys'))
print(d('values'))
