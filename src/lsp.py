class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


# Standardowe konto bankowe (można wypłacać całą kwotę)
class RegularAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise Exception("Insufficient funds")


# Konto oszczędnościowe z minimalnym saldem 100
class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self._min_balance = 100  # Minimalne saldo

    def withdraw(self, amount):
        if self._balance - amount >= self._min_balance:
            self._balance -= amount
        else:
            raise Exception("Minimum balance for savings account is 100")


# Funkcja transakcji obsługuje tylko konta, które obsługują wypłaty
def perform_transaction(account, deposit_amount, withdraw_amount):
    if not hasattr(account, "withdraw"):
        raise Exception("This account type does not support withdrawals")

    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    print(f"Balance after transaction: {account.get_balance()}")


# Użycie
regular_account = RegularAccount()
savings_account = SavingsAccount()

perform_transaction(regular_account, 500, 200)  # Działa
perform_transaction(savings_account, 500, 450)  # Exception!

print(f"Savings account balance: {savings_account.get_balance()}")