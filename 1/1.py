# types of tokens

# punctuators
# (), {}, @, [], #, etc.
# -=, +=, /=, *=, //=, =, etc.
# a*b+c
# (a*b)+c
# a*(b+c)

name="hiral"
age=18
print(name)
print(type(name))
print(age)
print(type(age))

# expression execution

A,B=2,3
Txt="@"
print(2*Txt*3)

A,B="2",3
Txt="@"
print((A+Txt)*B)    # concatenation

A,B=2,3
C=4
print(A+B*C)
# 2+3*4 # * > +
# 2+12=14

A,B=10,5.0
C=A*B
print(C)

A,B=1,2
C=A/B
print(C)

A,B=1.5,3
C=A//B
print(C,A/B)

# (A//B) == floor(A/B)

A,B=12,5
C=A//B
print(C)

A,B=-12,5
C=A//B
print(C)

A,B=12,-5
C=A//B
print(C)

A,B=-5,2
C=A%B
print(C)

A,B=5,2
C=A%B
print(C)

A,B=-5,-2
C=A%B
print(C)

# comments in python

# single line comment
"""
this is a multi-line comment
"""
# print("hello") -> wont be printed
print("hello") # -> will be printed

# input in python
# input()
# taking input from user & printing it
# string input
name=input("name : ")
print("hello",name)
# int input
age=int(input("age : "))
# float input
price=float(input("price : "))
print("my name is",name,"and i am",age,"years old.")

# practice time
# State True or False
"""
1) /* is a symbol used in Python for single line comment. -> False
2) 2ndName is an invalid identifier in Python. -> True
3) ** is a valid arithmetic operator in Python. -> True
4) in is a logical operator in Python. -> False
5) Variable declaration is implicit in Python. -> True
6) Consider the given expression: not True and False or True
    Which of the following will be correct output if the given expression is evaluated?
    (a) True (b) False (c) None (d) Null -> not > and > or -> (a) [True]
"""
# membership operators (in, not in)
# identity operators (is, is not)
# bitwise operators (&, |, ^)

# conditional statements
# traffic lights code
light=input("light colour : ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look get ready, go slow")
elif(light=="green"):
    print("go")
else:
    print("light is broken")
# grades of students
marks=int(input("marks : "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")

# practice time
"""
Print output for:
A = 5 & G = M
A = 2 & G = F
"""
A=int(input("A : "))
G=input("M/F : ")
if((A==1 or A==2) and G=="M"):
    print("fee is 100")
elif(A==3 or A==4 or G=="F"):
    print("fee is 200")
elif(A==5 and G=="M"):
    print("fee is 300")
else:
    print("no fee")

# single line if
# ternary operator
# <var> = <var1> if <condition> else <val2>
food=input("food : ")
eat="yes" if food=="cake" else "no"
print(eat)

# <stt1> if <condition> else <stt2>
food=input("food : ")
print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")

# clever if
# ternary operator
# <var> = (false_val,true_val) [<condition>]
age=int(input("age : "))
vote=("yes","no") [age<18]
sal=float(input("salary : "))
tax=sal*(0.1,0.2) [sal>50000]
print(tax)

# best practices
# calculate simple interest
a=float(input("a : "))
b=float(input("b : "))
c=float(input("c : "))
print(a*b*c/100)
# improved
p=float(input("p : "))
r=float(input("r : "))
t=float(input("t : "))
si=(p*r*t)/100
print(si)