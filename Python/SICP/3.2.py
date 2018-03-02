# Function and the generated process
# Recursive function
def pig_latin(w):
    """Return the Pig Latin equivalent of English word w."""
    if starts_with_a_vowel(w):
        return w + 'ay'
    return pig_latin(w[1:] + w[0])


def starts_with_a_vowel(w):
    """Return whether w begins with a vowel."""
    return w[0].lower() in 'aeiou'


print(pig_latin('pun'))


def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


print(fact_iter(4))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(4))


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def fib_iter(n):
    prev, curr = 1, 0  # curr is the first Fibonacci number.
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


def memo(f):
    """Return a memoized version of single-argument function f."""
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


fib = memo(fib)
print(fib(40))
