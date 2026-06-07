class Employee:
    role = input("enter the role : ")
    dept = input("enter the department : ")
    sal = float(input("enter the salary : "))
    def show_details(self):
        print(f"role : {self.role}")
        print(f"department : {self.dept}")
        print(f"salary : {self.sal}")
class Engineer(Employee):
    name = input("enter the name : ")
    age = int(input("enter the age : "))
    def show(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
engi = Engineer()
engi.show()
engi.show_details()