# Problem 1
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(
            f"hi {self.name},\nyour total balance after deposit is: {self.balance}\nThanks"
        )

    def withdraw(self, amount):
        if amount > self.balance:
            print("inffuciant balance sorry!!")
        else:
            self.balance -= amount
            print(
                f"hi {self.name},\nyour total balance after withdraw is: {self.balance}\nThanks"
            )


class SavingAccount(Account):
    def add_interst(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(
            f"interest on ur account balance is {interest} and now ur total balance is {self.balance}\nThanks"
        )


class CurruntAccount(Account):
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print(f"overdraft used! balance: {self.balance}")
        else:
            print(f"hi {self.name},\nyour balance is: {self.balance}")


A = Account("yuvraj", 2000)
S = SavingAccount("Yuvraj", 2000)
S.add_interst()
C = CurruntAccount("Yuvraj", 3000)
C.withdraw(500)
# A.deposit(500)
A.withdraw(300)
