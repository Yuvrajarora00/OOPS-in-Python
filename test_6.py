# employee salary system


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        if self.salary > 50000:
            bonus = self.salary * 0.20
            # print("bonus is", bonus)
        else:
            bonus = self.salary * 0.10
        return bonus
        # print("your bonus is :", bonus)

    def show_salary(self):
        total = self.salary + self.bonus()
        print(f"hi {self.name}, your salary is {total}\nthank you")


E = Employee("yuvraj", 73000)
print("bonus is:", E.bonus())
E.show_salary()
