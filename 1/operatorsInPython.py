# arithmetic operators
a=5
a=4
b=2
sum=a+b
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  # remainder
print(a**b) # a^b
# relational operators
a=50
b=20
print(a==b) # False
print(a!=b) # True
print(a>=b) # True
print(a>b)  # True
print(a<=b) # False
print(a<b)  # False
# assignment operators
num=10
# num=num+10
# 10+10=>20
num+=10
print("num: ",num)
num-=10
print(num)  # 0
num*=5
print(num)  # 50
num/=5
print(num)  # 2
num%=5
print(num)  # 0
num**=5
print(num)  # 1,00,000
# logical operators
a=50
b=30
print(not False)
print(not True)
print(not(a>b))
val_1=True
val_2=True
print("and operator: ",val_1 and val_2)
val_1=False
val_2=False
print("or operator: ",val_1 or val_2)
print((a==b) or (a>b))