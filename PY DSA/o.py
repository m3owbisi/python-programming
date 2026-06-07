try:
    num = int(input("enter an integer : "))
    result = 100 / num
    print(f"100 divided by {num} is {result}")
except ValueError:
    print("error : input is not a valid integer")
except ZeroDivisionError:
    print("error : division by zero is not allowed")