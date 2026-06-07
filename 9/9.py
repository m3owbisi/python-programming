# del keyword
# del s1.name
# del s1
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("shradha")
# print(s1.name)
# del s1.name
# print(s1.name)

# private (like) attributes & methods
# class Account:
#     def __init__(self,ac_no,ac_pass):
#         self.ac_no=ac_no
#         self.__ac_pass=ac_pass
#     def reset_pass(self):
#         print(self.__ac_pass)
# acc1=Account("12345","abcde")
# print(acc1.ac_no)
# # print(acc1.__ac_pass)
# print(acc1.reset_pass())
# class Person:
#     __name="anonymous"
#     def __hello(self):
#         print("hello person!")
#     def welcome(self):
#         __hello(self.name)
# p1=Person()
# print(p1.__name)
# print(p1.__hello())
# print(p1.welcome())

# inheritance
# class Car:
#       ...
# class ToyotaCar(Car):
#       ...
class Car:
    color="black"
    def create(self,type):
        print("car created..")
    def modify(self,model):
        print("car ready to be modified..")
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
class Fortuner(ToyotaCar):
    def __init__(self,type):
        # super method
        super().__init__(self)
        super().create(self)
        super().modify(self)
        self.type=type
class Prius(ToyotaCar):
    def __init__(self,model):
        # super method
        super().__init__(self)
        super().create(self)
        super().modify(self)
        self.model=model
car1=ToyotaCar("fortuner")
print(car1.brand)
print(car1.color)
print(car1.start())
print(car1.stop())
car1=Fortuner("diesel")
print(car1.start())
print(car1.stop())
car2=ToyotaCar("prius")
print(car2.brand)
print(car2.color)
print(car2.start())
print(car2.stop())
car2=Prius("petrol")
print(car2.start())
print(car1.stop())

class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

# class method
# class Student:
# @classmethod  # decorator
# def college(cls):
#     pass

class Person:
    name="anonymous"
    def changeName(self,name):
        # Person.name=name
        self.name=name
        # self.__class__.name="rahul"
    @classmethod
    def change_name(cls,name):
        cls.name=name
p1=Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)
p1.change_name("rahul kumar")
print(p1.name)
print(Person.name)

# property
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # percentage
        # self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    # def calcPercentage(self):
        # percentage
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
stud1=Student(98,97,99)
print(stud1.percentage)
stud1.phy=86
print(stud1.phy)
# stud1.calcPercentage()
print(stud1.percentage)

# polymorphism : operator overloading
# a+b # addition    a.__add__(b)
# a-b # subtraction a.__sub__(b)
# a*b # multiplication a.__mul____(b)
# a/b # division     a.__truediv____(b)
# a%b # modulus  a.__mod____(b)

print(type(1))
print(1+2)  # 3
print(type("apna"))
print("apna "+"college") # concatenate -> apna college
print(type([7,8,9]))
print([1,2,3]+[4,5,6]) # [1,2,3,4,5,6] -> merge

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def showNumber(self):
        print(self.real,"i +",self.imag,"j")
    def __add__(num1,num2):
        newReal=num1.real+num2.real
        newImag=num1.imag+num2.imag
        return Complex(newReal,newImag)
    def __sub__(num1,num2):
        newReal=num1.real-num2.real
        newImag=num1.imag-num2.imag
        return Complex(newReal,newImag)
num1=Complex(1,3)
num1.showNumber()
num2=Complex(4,6)
num2.showNumber()
# print(num1.showNumber())
# print(num2.showNumber())
# print(num1+num2)
# num3=num1.add(num2)
num3=num1+num2
num3.showNumber()
num3=num1-num2
num3.showNumber()

# lets practice
"""
Qs. Define a Circle class to create a circle with radius r using the constructor.
    Define an Area() method of the class which calculates the area of the circle.
    Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
"""
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius
c1=Circle(21)
print(c1.area())
print(c1.perimeter())
"""
Qs. Define a Employee class with attributes role, department & salary.
    This class also has a showDetails() method.
    Create an Engineer class that inherits properties from Employee & has additional
    attributes : name & age.
"""
class Employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("sal =",self.sal)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","i.t.","75,000")
e1=Employee("accountant","finance","60,000")
e1.showDetails()
engi1=Engineer("elon musk",40)
engi1.showDetails()
"""
Qs. Create a class called Order which stores item & its price.
    Use Dunder function __gt__() to convey that:
    order1 > order2  if price of order1 > price of order2
"""
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(order1,order2):
        return order1.price>order2.price
order1=Order("chips",20)
order2=Order("tea",15)
print(order1>order2)    # True