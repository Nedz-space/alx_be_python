# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the account with an optional initial balance.
        :param initial_balance: Starting balance for the account (default is 0).
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        :param amount: Amount to be deposited.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if funds are sufficient.
        :param amount: Amount to be withdrawn.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

