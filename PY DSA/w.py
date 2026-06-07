students = {554 : 'ajay', 350 : 'ramesh', 395 : 'rakesh'}
rollno = int(input("enter roll number : "))
name = students.get(rollno, 'student')
print(f"congratulations {name}!")
rollno = int(input("enter roll number : "))
name = students.get(rollno, 'student')
print(f"congratulations {name}!")