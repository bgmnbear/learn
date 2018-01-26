from urllib.request import urlopen

# Start
print('Hello, SICP!')

# Expressions and statements
shakespeare = urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')
words = set(shakespeare.read().decode().split())
print({w for w in words if len(w) >= 5 and w[::-1] in words})
