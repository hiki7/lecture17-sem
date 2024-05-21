class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Внесение наличных на счет: {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        self.__balance -= amount
        self.__transactions.append(f"Снятие наличных: {amount}")

    def add_interest(self):
        self.__balance *= self.__interest_rate
        self.__transactions.append(f"Начислены проценты по вкладу: {self.__balance}")

    def history(self):
        for transaction in self.__transactions:
            print(transaction)


account = BankAccount(100000, 0.05)
account.deposit(15000)
account.withdraw(7500)
account.add_interest()
account.history()

