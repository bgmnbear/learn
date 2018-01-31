# Iteration
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1  # Fibonacci numbers
    k = 2  # Position of curr in the sequence
    while k < n:
        pred, curr = curr, pred + curr  # Re-bind pred and curr
        k = k + 1  # Re-bind k
    return curr


print('---Iteration---')
print(fib(8))


# Test
def fib_test():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib(3) == 1, 'The 3nd Fibonacci number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'


fib_test()

# Doctest

from doctest import run_docstring_examples


def sum_naturals(n):
    """Return the sum of the first n natural numbers
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


run_docstring_examples(sum_naturals, globals())
