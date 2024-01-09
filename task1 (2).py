class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")


# Example usage:
account = BankAccount("John Doe", "1234567890")
account.deposit(1000)
account.withdraw(500)
account.display_balance()
