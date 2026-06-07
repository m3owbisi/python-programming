# functions in python
# def func_name(param1,param2,..):
#     # some work
#     return val
# func_name(arg1,arg2..)  # function call
# def sum(a,b):
#     s=a+b
#     return s
# print(sum(2,3))
# addition of two numbers
# more lines of code
a=5
b=10
add=a+b
print(add)
# more lines of code
a=2
b=8
add=a+b
print(add)
# more lines of code
a=12
b=17
add=a+b
print(add)
# addition of two numbers
def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
# more lines of code
calc_sum(5,10)
# more lines of code
calc_sum(2,8)
# more lines of code
calc_sum(12,17)
# function definition
def calc_diff(a,b): # parameters
    return a-b
diff=calc_diff(2,1)  # 1    # function call
print(diff)
diff=calc_diff(2221,178)    # 2043  # arguments
print(diff)
def print_hello():
    print("hello")
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
output=print_hello()
print(output)
# average of 3 numbers
def calc_avg(a,b,c):
#   if(a==0)
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
calc_avg(1,2,3)
calc_avg(98,97,95)
# print()
# len()
# type()
# range()
print("apna college","shradha khapra")  # sep " "   # end = "\n"
print("apna college",end=" ")
print("shradha khapra")
# len()
# type()
# range()
def calc_prod(a=0,b=0): # a=0,b -> a,b=0
    print(a*b)
    return a*b
calc_prod()

# lets practice
"""
WAF to print the length of a list. (list is the parameter)
"""
cities=["delhi","gurgaon","noida","pune","mumbai","chennai","bangalore"]
heroes=["thor","ironman","captain america","shaktiman","superman","spiderman","batman"]
def print_len(cities):
    print(len(cities))
print_len(cities)
print_len(heroes)
"""
WAF to print the elements of a list in a single line. (list is the parameter)
"""
heroes=["thor","ironman","captain america","shaktiman","superman","spiderman","batman"]
print(heroes[0],end=" ")
print(heroes[1],end=" ")
print("\n")
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)
print("\n")
print_list(heroes)
print("\n")
"""
WAF to find the factorial of n. (n is the parameter)
"""
# n=5
n=int(input("enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(n)
"""
WAF to convert USD to INR.
"""
def converter(usd_val):
    inr_val=usd_val*83.41
    print("$",usd_val,"usd =",inr_val,"inr")
usd_val=int(input("enter us dollar: $"))
converter(usd_val)

# recursion
# prints n to 1 backwards
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# recursive function
def show(n):
    # a=123
    if(n==0):
        return
    print(n)
    show(n-1)
    print("end")
show(5) # 5=n,4=n-1,3=n-2,2=n-3,1=n-4
print("\n")
# returns n!
# def fact(n):
#     if(n==0 or n==1):
#         return n    # return 0,1
#     else:
#         return n*fact(n-1)
def fact(n):
    if(n==1 or n==0):
        return n
    return fact(n-1)*n
print(fact(7))
print("\n")

# lets practice
"""
Write a recursive function to calculate the sum of first n natural numbers.
"""
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
print(calc_sum(3))
print("\n")
"""
Write a recursive function to print all the elements in a list.
Hint: use list & index as parameters
"""
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","litchi","apple","banana"]
print_list(fruits)
print("\n")