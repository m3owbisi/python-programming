print(3>2)
print(3<2)
print(3>=2)
print(3<=2)
print(3==2)
print(3==3)
print(3!=2)
print(3!=3)
#   or
print(2>3 or 2>1)
#   and
print(3>2 and 2>1)
print(3>2 and 2>6)
#   not
print(2>3)
print(not 2>3)
print(3>2)
print(not 3>2)
age=19
# age=16
# age=13
# age=2
if age>=18:
    print("you are an adult")
    print("you can vote")
    print("you are old enough to live on your own")
elif age<18 and age>3:
    print("you are in school")
    print("you are a teenager")
else:
    print("you are a child/kid")
print("thank you")