class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number
    


account = BankAccount("123456789", 1000)

# Attempt to access private attributes directly (this will raise an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing balance using the public method
print(account.get_balance())  # Output: 1000

# Depositing money
account.deposit(500)  # Output: Deposited 500. New balance is 1500

# Withdrawing money
account.withdraw(200)  # Output: Withdrew 200. New balance is 1300

# Attempting to withdraw more than available balance
account.withdraw(2000)  # Output: Invalid withdrawal amount or insufficient funds

