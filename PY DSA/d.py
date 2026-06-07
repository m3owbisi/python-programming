class Number:
    def get_number(self):
        self.number = int(input("enter the number : "))
    def set_number(self):
        print(f"the number is set : {self.number}")
    def is_negative(self):
        if self.number < 0:
            print("number is negative")
        else:
            print("number is positive")
    def is_divisible_by(self):
        self.n = int(input("enter the divisor : "))
        if self.number % self.n == 0:
            print(f"{self.number} is divisible by {self.n}")
        else:
            print(f"{self.number} is not divisible by {self.n}")
    def absolute_value(self):
        s = abs(self.number)
        print(s)
num = Number()
num.get_number()
num.set_number()
num.is_negative()
num.is_divisible_by()
num.absolute_value()