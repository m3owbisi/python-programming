# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("start")
# print(multiply(1, 2, 3))
# print("finish")

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print("we have {count} even numbers")