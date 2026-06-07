# loops in python
# while condition:
    # some work
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("\n")
# while True:
#     print("hello")
count=1
while count<=5:
    print("hello")
    # count=count+1
    count+=1
print("\n")
print(count)
print("\n")
i=1
while i<=5: # 100 # 10000
    print("apna college",i)
    i+=1
print("\n")
# print numbers from 1 to 5
i=1
while i<=5:
    print(i)
    i+=1
print("ended the loop")
print("\n")
i=5
while i>=1:
    print(i)
    i-=1
print("ended the loop")
print("\n")

# lets practice
"""
Print numbers from 1 to 100.
"""
i=1
while i<=100:   # stopping condition
    print(i)
    i+=1
print("\n")
"""
Print numbers from 100 to 1.
"""
i=100
while i>=1:
    print(i)
    i-=1
print("\n")
"""
Print the multiplication table of a number n.
"""
n=int(input("enter a number: "))
i=1
while i<=10:
    print(n,"X",i,"=",n*i)
    i+=1
"""
Print the elements of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]
"""
nums=[1,4,9,16,25,36,49,64,81,100]
print("\n")
print(nums[0])  # ..print(nums[9])..print(nums[len(nums)-1])
print("\n")
# [len(nums)] -> 10 -> 1 -> 9
idx=0
# while idx<=len(list)-1
# while idx<len(list)
while idx<len(nums):
    # print(idx)
    print(nums[idx])    # nums[0],..nums[9]
    idx+=1
print("\n")
# heroes=["ironman","thor","superman","batman","spiderman"]
# traverse
# i=0
# while i<len(heroes):
#     print(heroes[i])
#     i+=1
"""
Search for a number x in this tuple using loop:
(1,4,9,16,25,36,49,64,81,100)
"""
nums=(1,4,9,16,25,36,49,64,81,100)
i=0 # initialization
x=100
while i<len(nums):
    print(nums[i])
    if(nums[i]==x):
        print("found at idx: ",i)
        break
    else:
        print("finding..")
    i+=1
print("end of loop")
print("\n")

# break and continue
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")
print("\n")
i=1
while i<=5:
    if(i==3):
        i+=1    
        continue    # skips
    print(i)
    i+=1
print("end of loop")
print("\n")
# i%2!==0

# for el in list:
    # some work
# list=[1,2,3]
# for el in list:
#     print(el)
# for el in list:
    # some work
# else:
#     work when loop ends
# for el in list:
#     print(el)
# else:
#     print("end")
nums=[1,2,3,4,5]
for val in nums:
    print(val)
print("\n")
vegetables=["potato","brinjal","ladyfinger","tomato","cucumber"]
for veggies in vegetables:
    print(veggies)
print("\n")
tup=(0,1,2,3,4,5,6,7,8,9)
for num in tup:
    print(num)
print("\n")
str="apnacollege"
for char in str:
    print(char)
    print("\t")
else:
    print("end of string")
print("\n")
# str="apnacollege"
# for char in str:
#   if(char=='a'):
#       print("a found")
#       break
#   print(char)
#   print("\t")
# else:
#     print("end of string")
# print("\n")

# lets practice
# using for
"""
Print the elements of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]
"""
nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)
print("\n")
"""
Search for a number x in this tuple using loop:
(1,4,9,16,25,36,49,64,81,100)
"""
nums=(1,4,9,16,25,36,49,64,81,100)
idx=0
x=100
for el in nums:
    if(el==x):
        print(el)
        print("number found at idx: ",idx)
        break
    else:
        print(el)
        print("finding..")
    idx+=1
print("\n")

# range()
# range(start?,stop,step?)
for el in range(5):
    print(el)
print("\n")
for el in range(1,5):
    print(el)
print("\n")
for el in range(1,5,2):
    print(el)
print("\n")
print(range(5))
seq=range(5)
print("\n")
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
print("\n")
for i in range(10): # range(stop)
    print(i)
print("\n")
for i in range(1,11):   # range(start,stop)
    print(i)
print("\n")
for i in range(0,11,2): # range(start,stop,step)
    print(i)
print("\n")
for i in range(1,100,2):
    print(i)
print("\n")
for i in range(2,101,2):
    print(i)
print("\n")

# lets practice
# using for & range()
"""
Print numbers from 1 to 100.
"""
for i in range(1,101):
    print(i)
print("\n")
"""
Print numbers from 100 to 1.
"""
for i in range(100,0,-1):
    print(i)
print("\n")
"""
Print the multiplication table of a number n.
"""
n=int(input("enter a number: "))
for i in range(1,11):
    print(n,"X",i,"=",n*i)
print("\n")

# pass statement
# for el in range(10):
#     pass
for i in range(5):
    # empty
    pass
    # no work needs to done
if i>5:
    pass
print("some useful work")
print("\n")

# lets practice
"""
WAP to find the sum of first n natural numbers. (using while)
"""
n=int(input("enter a number: "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("total sum is: ",sum)
print("\n")
"""
WAP to find the factorial of first n numbers. (using for)
"""
n=int(input("enter a number: "))
i=1
fact=1
for i in range(1,n+1):
    fact*=i
    i+=1
print("factorial of",n,"is: ",fact)
print("\n")