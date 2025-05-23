class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")

    def transfer(self, target_account, amount: float):
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transaction_history.append(f"Transferred {amount} to {target_account.owner}")

    def rename_owner(self, new_owner: str):
        if not new_owner.strip():
            raise ValueError("Owner name cannot be empty")
        self.owner = new_owner
        self.transaction_history.append(f"Renamed owner to {new_owner}")

    def get_summary(self):
        return {
            "owner": self.owner,
            "balance": self.balance,
            "transactions": self.transaction_history.copy()
        }

if __name__ == "__main__":

    a = BankAccount("Alice", 100.0)
    b = BankAccount("Bob", 50.0)

    a.deposit(50)           
    a.withdraw(20)          
    a.transfer(b, 50)       
    a.rename_owner("Alina") 

    print("Итоговая информация по счёту:")
    summary = a.get_summary()
    print(f"Владелец: {summary['owner']}")
    print(f"Баланс: {summary['balance']}")
    print("Транзакции:")
    for entry in summary["transactions"]:
        print(f" - {entry}")
