# oop in python
a=10
b=20
sum=a+b
print(sum)
diff=a-b
print(diff)
prod=a*b
print(prod)
quotient=a/b
print(quotient)
remainder=a%b
print(remainder)
# class & object in python
# creating class
# class Student:
#     name="karan kumar"
# creating object (instance)
# s1=Student()
# print(s1.name)
# ["karan kumar",94.4]
class Student:
    name="karan"
s1=Student()
print(s1)
print(s1.name)
s2=Student()
print(s2.name)
class Car:
    color="blue"
    model="mercedes"
    brand="gyat"
car1=Car()
print(car1.color)
print(car1.model)
print(car1.brand)
# __init__ function
# creating class
# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
# creating object
# s1=Student("karan")
# print(s1.name)
class Student:
    college_name="somaiya college"
    fullname="anonymous"    # obj.attr > Class attr
    # default constructor
    def __init__(self):
        pass
    # parameterized constructor
    def __init__(self,fullname,mark):
        print(self)
        self.fullname=fullname
        self.mark=mark
        print("adding new student in database..")
    def welcome(self):
        print("welcome student,",self.fullname)
print(Student.college_name)
s1=Student("karan",97)
print(s1)
print(s1.college_name)
print(s1.fullname)
print(s1.mark)
s1.welcome()
s2=Student("arjun",88)
print(s2)
print(s2.college_name)
print(s2.fullname)
print(s2.mark)
s2.welcome()

# class & instance attributes
# Class.attr
# obj.attr
# methods
# creating class
# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
#     def hello(self):
#         print("hello",self.name)
# creating object
# s1=Student("karan")
# s1.hello()

# lets practice
"""
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
"""
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    # @staticmethod
    # def hello():
    #     print("hello")
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"your avg score is:",sum/3)
s1=student("tony stark",[99,98,97])
s1.get_avg()
s1.name="batman"
s1.get_avg()

# static methods
# class Student:
#       @staticmethod   # decorator
#       def college():
#           print("abc college")

# important
# abstraction
# encapsulation
# inheritance
# polymorphism
class Car:
    def __init__(self):
        self.accelerator=False
        self.brake=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.accelerator=True
        print("car started..")
car1=Car()
car1.start()
# lets practice
"""
Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.
"""
class Account:
    def __init__(self,bal,ac_no):
        self.balance=bal
        self.account_no=ac_no
    # debit method
    def debit(self,amount):
        self.balance-=amount
        print("debit rs.",amount,"amount was debited from your account")
        print("total balance =",self.get_balance())
    # credit method
    def credit(self,amount):
        self.balance+=amount
        print("credit rs.",amount,"amount was credited to your account")
        print("total balance =",self.get_balance())
    def get_balance(self):
        # print("your balance is:",self.balance)
        return self.balance
acc1=Account(10000,12345)
print(acc1.balance,acc1.account_no)
acc1.debit(1000)
acc1.credit(50500)