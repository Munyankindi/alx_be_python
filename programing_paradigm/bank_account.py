class BankAccount:
    def __init__(self,account_balance = 0):
        self.__account_balance = account_balance
    def deposit (self,amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be Positive")
    def withdraw (self,amount):
        self.amount = amount
        if amount <=0:
            print("withdrawal amount should be positive")
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print(f"Insufficient Balance")
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")

account = BankAccount()
account.deposit(50)
account.withdraw(80)
account.display_balance()