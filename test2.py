# practice 2


class Bank:

    def __init__(self, money):
        self.money = money

    def dep(self, money):
        self.money += money
        print("the available amount is: ", self.money)
        print(self.money)

    def widrow(self, money):
        self.money -= money
        print("balance in your account is: ", self.money)
        print(self.money)

    def balance(self):
        return self.money


b1 = Bank(1000)
b1.dep(500)
b1.widrow(300)

print("the balance is: ", b1.balance())
