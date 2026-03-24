class Student:
    def __init__(
        self, name, marks
    ):  # __name this is called private atribute front __ this
        self.__name = name
        self.__marks = marks

    def set_data(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_data(self):
        print(f"name = {self.__name}")
        print(f"marks = {self.__marks}")

    def grade(self):
        if self.__marks >= 90:
            grade = "A+"
        elif self.__marks >= 80:
            grade = "A"
        elif self.__marks >= 70:
            grade = "B"
        elif self.__marks >= 60:
            grade = "C"
        else:
            grade = "low Grade"
        print(
            f"Hi {self.__name} your marks is {self.__marks} and your Grade is {grade}"
        )


S = Student("Yuvraj", 80)
S.get_data()
S.grade()
print("-------------------------------------------------------------")
S.set_data("karan", 67)
S.get_data()
S.grade()
