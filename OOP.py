# practice que 1
# class students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(f"hi {self.name} your avg score is: {sum/3}")


# s1 = students("yuvraj", [43, 65, 36])
# s1.avg()


# Practice que 2


class bank:
    def __init__(self, amount, acc_no):
        self.amount = amount
        self.acc_no = acc_no

    def debit(self, amount):
        self.amount -= amount
        print("debited amount is: ", amount)
        print("totall balance in your account is: ", self.get_amount())

    def credit(self, amount):
        self.amount += amount
        print("your credited amount is: ", amount)
        print("total amout in your account is: ", self.get_amount())

    def get_amount(self):
        return self.amount


# user input
amount = int(input("enter amount: "))
acc_no = int(input("enter account number: "))

acc1 = bank(amount, acc_no)

# enter selection
print("/nselect option: ")
print("1. debit")
print("2. credit")

choice = int(input("enter your choice: "))

# if else
if choice == 1:
    debt_amt = int(input("enter amount you want to debit: "))
    acc1.debit(debt_amt)

elif choice == 2:
    credit_amt = int(input("enter amount u wanbt to credit: "))
    acc1.credit(credit_amt)

else:
    print("invalid option")
