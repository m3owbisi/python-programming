num1 = float(input("enter the first number1 : "))
num2 = float(input("enter the second number2 : "))
num3 = float(input("enter the third number3 : "))
if num1 >= num2 and num1 >= num3:
    largest = num1
    print("num1 is greatest")
elif num2 >= num1 and num2 >= num3:
    largest = num2
    print("num2 is greatest")
else:
    largest = num3
    print("num3 is greatest")
print(f"the largest number is {largest}")