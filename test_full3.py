# problem 9
a = int(input("enter a number: "))

b = a * a
print("square is: ", b)


# problem 10
a = input("enter a string: ")
if a == a[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")


# problem 11
class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print("brand is : ", self.brand)
        print("top spees is : ", self.speed)


C1 = Car("toyota", 340)
C1.show_details()


# problem 12


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            print("A Grade ")

        elif self.marks >= 80:
            print("B Grade")

        elif self.marks >= 70:
            print("C Grade")

        else:
            print("pass")
        print(self.name)
        print(self.marks)


S1 = Student("karan", 60)
S1.grade()


# problem 13
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("your balance is: ", self.cheak_bal())

    def withdrow(self, amount):
        if amount > self.balance:
            print("low balance...!")
        else:
            self.balance -= amount
            print("you balance is: ", self.cheak_bal())

    def cheak_bal(self):
        return self.balance


B1 = Bank(500)
B1.deposit(200)
B1.withdrow(300)
print(B1.cheak_bal())
