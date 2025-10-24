class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Деньги на счету\nна счету {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Снято {amount}\nОстаток {self.balance}")
        else:
            print("Сумма выше баланса")

    def show_balance(self):
        print(f"баланс: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = []

    def add_acc(self, account):
        self.accounts.append(account)

    def search_acc(self, owner_name):
        for account in self.accounts:
            if account.owner == owner_name:
                return account
        return None
        
    def transfer(self, from_account, to_account, amount):
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"Перевод {amount} выполнен")
        else:
            print("Недостаточно средств для перевода")







    
