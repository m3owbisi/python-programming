# mini project
# guess the number
import random
# randNum=random.randint(1,6)
# print(randNum)
target=random.randint(1,6)
while True:
    # userChoice=int(input("guess the target : "))
    userChoice=(input("guess the target or quit (q) : "))
    if(userChoice=="q"):
        break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("you win ! success : correct guess !!!")
        break
    elif(userChoice<target):
        print("your guess is/was too low/small.")
        print("take a bigger guess..")
        print("guess again")
    else:
        print("your guess is/was too high/large.")
        print("take a smaller guess..")
        print("guess again")
print("--------game over--------")

# random password generator
import random
import string
# val=random.choice([1,2,3,4,5])
# print(val)
# val=random.choice(['a','b','c','d','e'])
# print(val)
# print(type(string.ascii_letters))
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)
# print(random.choice("hello"))
charVal=string.ascii_letters+string.digits+string.punctuation
# print(charVal)
# print(random.choice(charVal))
password=""
pass_len=8
for i in range(pass_len):
    # print(random.choice(charVal))
    password+=random.choice(charVal)
print("your random password is",password)

# list comprehension
# [function for i in range(n)]
password="".join([random.choice(charVal) for i in range(pass_len)]) # -> arcx
print("your random password is",password)
# num3.showNumber()