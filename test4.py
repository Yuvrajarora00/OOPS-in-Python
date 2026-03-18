class Wallet:

    def __init__(self, money):
        self.money = money

    def add_money(self, amount):
        self.money += amount
        print(amount)
        print(self.cheak_money())

    def purchase(self, amount):
        if amount > self.money:
            print("infuciant balance..!")
        else:
            self.money -= amount
            print("amount: ", amount)
            print(self.cheak_money())

    def cheak_money(self):
        return self.money


C1 = Wallet(500)

C1.add_money(200)

# C1.add_money(300)
C1.purchase(500)

print(C1.cheak_money())
