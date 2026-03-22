del function


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = student("yuvraj", 53)
del s1.age  # to delete the object properties

print(s1.name, s1.age)  # now this will give error


# the use of @staticmethod
# in @static method we dont have to use self. it dont get error

# and  in this code we also use single inheritance like our 2 functions start and stop is also in other class named fortuner.


class car:
    @staticmethod
    def start():
        print("car starting...")

    @staticmethod
    def stop():
        print("car stops...")


class fortuner(car):
    def __init__(self, name):
        self.name = name


car1 = fortuner("fortuner")
car2 = fortuner("ford")

print(car1.name)


# multi-level inheritance


class car:
    @staticmethod
    def start():
        print("car starting...")

    @staticmethod
    def stop():
        print("car stops...")


class toyotacar(car):
    def __init__(self, brand):
        self.brand = brand


class fortuner(toyotacar):
    def __init__(self, type):
        self.type = type


car1 = fortuner("petrol")
car1.start()


# multiple inheritance


class one:
    def __init__(self):
        self.name = "yuvraj"


class two:
    def hello(self):
        self.age = 23


class three(one, two):
    def hello1(self):
        self.clas = "10th"


c1 = three()

c1.hello()
c1.hello1()

print(c1.name)
print(c1.age)
print(c1.clas)
