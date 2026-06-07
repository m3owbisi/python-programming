print("Mini-Project")
print("Exercise")
print("If-else")
print("Let's Build a calculator")
print("a + b")
print("a - b")
print("a * b")
print("a / b")
# print("a % b")
first=input("enter first number: ")
operator=input("enter operator (+,-,*,/,%): ")
second=input("enter second number: ")
first=int(first)
second=int(second)
if operator=='+':
    print(first+second)
elif operator=='-':
    print(first-second)
elif operator=='*':
    print(first*second)
elif operator=='/':
    print(first/second)
elif operator=='%':
    print(first%second)
else:
    print("invalid operation")