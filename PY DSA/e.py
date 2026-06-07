class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    def age(self):
        self.age = 2024 - self.dob
        print(f"age of {self.name} is {self.age}")
person = Person("hiral", "india", 2005)
person.age()