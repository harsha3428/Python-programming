'''Write a program to create an abstract class Shape with abstract methods
calculateArea() and calculatePerimeter(). Create subclasses Circle and Triangle 
that extend the Shape class and implement the respective methods to calculate 
the area and perimeter of each shape'''

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 
    def calculate_area (self):
        return 3.14 * (self.radius)**2
    def calculate_perimeter(self):
        return 2*3.14* self.radius
class Triangle(Shape):
    def __init__(self,base,height,side1,side2,side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_area(self):
        return 0.5 * self.base * self.height
    def calculate_perimeter(self):
        return (self.side1 + self.side2 + self.side3)
    
r = 54
circle = Circle(r)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

print("Radius of the circle : ", r)
print("Circle Area:",circle_area)
print("Circle Perimeter: ",circle_perimeter)


base = 5
height = 8
s1 = 6
s2 = 7
s3 = 8

print("\nTriangle :Base = ",base, "\nHeigth = ", height,"\nSide 1 = ",s1,"\nSide 2 = ",s2, "\nSide3 = ",s3)
triangle = Triangle(base, height, s1, s2,s3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimeter()

print("Triangle Area: ", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)