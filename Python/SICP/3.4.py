from math import sqrt


def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta) - f(x)
    return df / delta


def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)

    return update


def invert(x):
    result = 1 / x  # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result


def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)


class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess


def iter_improve(update, done, guess=1, max_updates=1000):
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return guess
    except ValueError:
        raise IterImproveError(guess)


def find_root(f, guess=1):
    def done(x):
        return f(x) == 0

    try:
        return iter_improve(newton_update(f), done, guess)
    except IterImproveError as e:
        return e.last_guess


if __name__ == '__main__':
    # invert(2)
    # print(invert_safe(0))
    print(find_root(lambda x: 2 * x * x + sqrt(x)))
