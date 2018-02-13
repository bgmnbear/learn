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
