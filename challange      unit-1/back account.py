Class BankAccount:
    Def __init__(self, account_number, account_holder_name, initial_balance):
        Self._account_number = account_number
        Self._account_holder_name = account_holder_name
        Self._account_balance = initial_balance

    Def deposit(self, amount):
        If amount > 0:
            Self._account_balance += amount
            Print(f”Deposited ${amount}. New balance: ${self._account_balance}”)
        Else:
            Print(“Invalid deposit amount. Please deposit a positive amount.”)

    Def withdraw(self, amount):
        If amount > 0 and amount <= self._account_balance:
            Self._account_balance -= amount
            Print(f”Withdrew ${amount}. New balance: ${self._account_balance}”)
        Elif amount <= 0:
            Print(“Invalid withdrawal amount. Please withdraw a positive amount.”)
        Else:
            Print(“Insufficient funds for withdrawal.”)

    Def display_balance(self):
        Print(f”Account Balance for {self._account_holder_name}: ${self._account_balance}”)

My_account = BankAccount(“123456789”, “John Doe”, 1000)

My_account.display_balance()
My_account.deposit(500)
My_account.withdraw(200)
My_account.withdraw(1500)
     
