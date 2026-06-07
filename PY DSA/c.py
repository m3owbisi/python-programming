class Calculator:
    num1 = int(input("enter the first number : "))
    num2 = int(input("enter the second number : "))
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
class Show(Calculator):
    def show(self):
        print(f"addition : {self.num1} + {self.num2} = {self.add()}")
        print(f"subtraction : {self.num1} - {self.num2} = {self.sub()}")
        print(f"multiplication : {self.num1} * {self.num2} = {self.mul()}")        
        print(f"division : {self.num1} / {self.num2} = {self.div()}")
cal = Calculator()
s = Show()
cal.add()
cal.sub()
cal.mul()
cal.div()
s.show()