# A simple bank account using a class

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount, "- Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance -= amount
            print("Withdrew", amount, "- Balance:", self.balance)


account = BankAccount("Ashish", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
