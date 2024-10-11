#Object Oriented Programming Challenge
'''
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class Account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amount):
        print(f"Avilable Balance: {self.balance}")
        self.balance = self.balance + dep_amount
        print(f"After deposit blance: {self.balance}")

    def withdraw(self,w_amount):
        print(f"Avilable Balance: {self.balance}")
        if self.balance >= w_amount:
            self.balance = self.balance - w_amount
            print(f"After withdraw blance: {self.balance}")
        else:
            print("Not sufficent balance!")
    def __str__(self):
        return f"Name of the account holder: {self.owner} and avilable balance: {self.balance}"

c1 = Account("Melvin",50000)
c1.deposit(400)
c1.withdraw(800000)
print(c1)
