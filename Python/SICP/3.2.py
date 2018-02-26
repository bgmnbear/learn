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
