n = 3
with open('example.txt', 'r') as file:
    for i in range(n):
        line = file.readline()
        print(line, end = ' ')