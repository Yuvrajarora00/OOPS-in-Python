class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def cheak_pin(self, pin):
        self.pin = self.pin
        if pin == self.pin:
            print("right pin")
            self.menu()
        else:
            print("pin is wrong")

    def menu(self):
        print("1. Deposits")
        print("2. Withdraw")
        print("3. Exit")

        choice = int(input("enter choice [1,2,3]: "))
        if choice == 1:
            amount = int(input("enter amount to deposit: "))
            self.deposit(amount)
        elif choice == 2:
            amount = int(input("enter amount to withdraw: "))
            self.withdraw(amount)
        elif choice == 3:
            print("Thank you")
        else:
            print("invalid number")

    def deposit(self, amount):
        self.balance += amount
        print("deposited: ", amount)
        print("balance", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("inffuciant balance")
        else:
            self.balance -= amount
            print("withdraw: ", amount)
            print("balance: ", self.balance)


a = int(input("enter your pin of 4 digits: "))

atm = ATM(5000, 3445)
atm.cheak_pin(a)
