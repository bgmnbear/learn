# OOP
class Account(object):
    # A class attribute
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


a = Account('Jim')
print(a.holder)
print(a.balance)

b = Account('Jack')
b.balance = 200
print([acc.balance for acc in (a, b)])

tom_account = Account('Tom')
print(tom_account.deposit(100))
print(tom_account.withdraw(90))
print(tom_account.withdraw(90))
print(tom_account.holder)

print(getattr(tom_account, 'balance'))
print(hasattr(tom_account, 'deposit'))

print(type(Account.deposit))
print(type(tom_account.deposit))

print(Account.deposit(tom_account, 1001))
print(tom_account.deposit(1000))

# Class attribute
jim_account = Account('Jim')
print(tom_account.interest, jim_account.interest)

Account.interest = 0.04
print(tom_account.interest, jim_account.interest)

jim_account.interest = 0.08
print(jim_account.interest)
print(tom_account.interest)


# Inherit
class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


checking = CheckingAccount('Sam')
print(checking.deposit(10))
print(checking.withdraw(5))
print(checking.interest)


# Multiple inheritance
class SavingsAccount(Account):
    deposit_charge = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # A free dollar!


such_a_deal = AsSeenOnTVAccount("John")
print(such_a_deal.balance)
print(such_a_deal.deposit(20))
print(such_a_deal.withdraw(5))

print(such_a_deal.deposit_charge)
print(such_a_deal.withdraw_charge)
