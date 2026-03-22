class Mobile:
    def __init__(self, balance):
        self.balance = balance

    def recharge(self, amount):
        self.balance += amount
        print(amount)
        print("your balance is : ", self.balance)

    def call(self, minutes):
        cost = minutes * 2
        if cost > self.balance:
            print("infuccient balance")
        else:
            self.balance -= cost
            print("minutes", minutes)
            print("cost is: ", cost)
            print("balance", self.balance)

    def show_balance(self):
        return self.balance


M1 = Mobile(100) # already 100 rupee in phone 

M1.recharge(50)  # we reacharge our mobile of 50 rupee

M1.call(30) # this means we make call of 30 minutes 

print("final balance is: ", M1.show_balance())
