# type conversion
a,b=1,2.0
sum=a+b
print(sum)
# error
# a,b=1,"2"     -> "str"
# b=int("2")
# sum=a+b
# print(type(a))
# print(type(b))
# print(a+b)
# print(sum)
a=2
b=4.25
sum=a+b # 2.0+4.25=>6.25
print(type(a))
print(type(b))
print(sum)
# type casting
a,b=1,"2"
c=int(b)
sum=a+c
print(sum)
# float()
a=3.14
a=str(a)
print(type(a))