class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        Area = self.pi * (self.radius ** 2)
        print(f"the area of the circle is : {Area}")
    def perimeter(self):
        Perimeter = 2 * self.pi * self.radius
        print(f"the perimeter of the circle is : {Perimeter}")
circle = Circle(4)
circle.area()
circle.perimeter()