# create a bank account

# create a forst class called bank account 

class BankAccount:
    def __init__(self,account_holder ="", account_number = 0, password = ""):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0
        self.password = password
        self.is_active = True

    def deposit(self,amount):
        self.balance = self.balance + amount
        return f"Avilabile balace is: {self.balance}."
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            return f"Invalid  Balance.."
        return f"Avilabile balace is: {self.balance}."

    def check_balance(self):
        return f"Avilabile balace is: {self.balance}."
    
    def close_account(self):
        self.is_active = False
        return f"{self.account_number} is inactive."

#create a object of BankAccount    
account_1 = BankAccount()
#ask the necessary detials from user to verify the account.
account_1.account_holder = input("Enter the Account Holder Name: ")
account_1.account_number = int(input("Enter the Account Number: "))
account_1.password = input("Enter the Password: ")


loop = True
while loop:
    #Asking user where deposit, withdraw, check balance or close account
    ask_users = input("What Operation Need... deposit, withdraw, check balance or close account: ").lower()

    if ask_users == "deposit":
        print(account_1.deposit(float(input("Enter the deposit Money: "))))
    elif ask_users == "withdraw":
        print(account_1.withdraw(float(input("Enter the withdraw Money: "))))
    elif ask_users == "check balance":
        print(account_1.check_balance())
    elif ask_users == "close account":
        print(account_1.close_account())
    else:
        print("Invalid Option...")
    
    #ask the user need to continue or not
    ask_continue = input("Enter Yes if want Continue else Enter No...").lower()
    if ask_continue == "no":
        loop = False   #exit the loop bcz it make the loop false.
