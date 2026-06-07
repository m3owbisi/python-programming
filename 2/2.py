# strings
# 'this is apna college's tutorial'
# "this is apna college's tutorial"
str1='apna \t college'
str2=" this is a string. \n we are creating it in python."
str3="""this is a string."""
print(str2)
# basic operations
# concatenation
# "hello" + "world" -> "helloworld"
print("hello"+"world")
string1="apna"
string2="college"
print(string1+string2)
final_string=string1+" "+string2
print(final_string)
# length of str
# len(str)
str="hiral"
print(len(str))
length1=len(string1)
length2=len(string2)
length=len(final_string)
print(length1)
print(length2)
print(length)



# indexing
str="Apna_College"
# str[0]='A',
# str[1]='p',...
# str[0]='B'  # not allowed
ch=str[0]
print(ch)
ch=str[1]
print(ch)
ch=str[2]
print(ch)
ch=str[3]
print(ch)
print(str[4])
# str[4]="-"    X
# str[4]="@"    X



# slicing
# str[starting_idx:ending_idx]    # ending idx is not included
str="ApnaCollege"
# str[1:4]="pna"
print(str[0:4])
print(str[1:4])
print(str[4:12])
# str[1:]==str[1:len(str)]
print(str[4:len(str)])
# str[:4]==str[0:4]
print(str[:4])
# [0:4]
# str[4:]==str[4:len(str)]
# [4:12]

# negative index
str="Apple"
# str[-3:-1]="pl"
print(str[-3:-1])
print(str[-5:-2])



# string functions
str="i am a coder."
str.endswith("er.") # returns true if string ends with substr
str.capitalize()    # capitalizes 1st char
# str.replace(old,new)    # replaces all occurences of old with new
# str.find(word)  # returns 1st index of 1st occurence
str.count("am") # counts the occurence of substr in string
string="i uh am studying python from uh apna college"
print(string.endswith("college"))
print(string.endswith("apna"))
print(string)
string=string.capitalize()
print(string)
print(string.capitalize())
print(string.replace("o","a"))
print(string.replace("python","java"))
print(string.find("python"))
print(string.find("java"))
print(string.count("uh"))



# lets practice
"""
WAP to input user's first name & print its length.
"""
name=input("enter your name: ")
print("length of your name is: ",len(name))
"""
WAP to find the occurence of '$' in a String.
"""
str="hi, $ i am the $ symbol $99.99"
print(str.count("$"))



# conditional statements
# if-elif-else (syntax)
# if(condition):
#   Statement1
# elif(condition):
#     Statement2
# else:
#      StatementN
# indentation
age=21
if(age>=18):    # (True)
    print("can vote and apply for license")
    print("can drive and can vote")
    print("can vote")
    print("can drive")
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("go slow")
else:
    print("look")
    print("light is broken")
print("end of code")
num=5
if(num>2):
    print("greater than 2")
if(num>3):
    print("greater than 3")
elif(num>4):
    print("greater than 4")
age=24
if(age>=18):
    print("can vote")
else:
    print("cannot vote")

# statements
mark=77
mark=int(input("enter student mark: "))
if(mark>=90):
    grade="A"
elif(mark>=80 and mark<90):
    grade="B"
elif(mark>=70 and mark<80):
    grade="C"
else:
    grade="D"
print("grade of the student -> ",grade)
# nesting
age=34
if(age>=18):
    print("can drive")
    if(age>=80):
        print("cannot drive")
else:
    print("cannot drive")



# lets practice
"""
WAP to check if a number entered by the user is odd or even.
"""
num=14
num=int(input("enter number: "))
rem=num%2
if(rem==0): # num%2==0
    print("even")
else:
    print("odd")
"""
WAP to find the greatest of 3 numbers entered by the user.
"""
# num=12,34,56
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if(num1>=num2 and num1>=num3):
    print("first number is greatest or largest, ",num1)
elif(num2>=num3):
    print("second number is greatest or largest, ",num2)
else:
    print("third is greatest or largest, ",num3)
"""
WAP to check if a number is a multiple of 7 or not.
"""
x=int(input("enter number (x): "))
if(x%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")