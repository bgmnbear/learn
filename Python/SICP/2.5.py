# OOP


class Account(object):
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
