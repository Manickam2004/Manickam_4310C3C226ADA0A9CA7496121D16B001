'''Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.'''

#Here's a Python implementation of the BankAccount class as you described:

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ₹{self.__account_balance}")


# Example usage:
if __name__ == "__main__":
    # Creating a BankAccount instance
    my_account = BankAccount("1234567890", "Sanjay", 1000.67)
    # Display balance
    my_account.display_balance()
    # Deposit money
    my_account.deposit(500.0)

    # Withdraw money
    my_account.withdraw(200.0)

    # Display balance
    my_account.display_balance()