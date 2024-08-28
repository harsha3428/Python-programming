'''You are developing a system to handle different shapes. Implement an abstract
class called Shape with an abstract method calculateArea(). The calculateArea()
method should be implemented by the concrete classes that inherit from Shape
and should return the area of the specific shape.
Create two concrete classes Circle and Rectangle that extend the Shape class.
Implement the calculateArea() method in both classes according to the area
calculation formulas for circles and rectangles. Display the areas of a circle and
a rectangle object.
Write the abstract class Shape, the concrete classes Circle and Rectangle, and
the code to display the areas.'''


from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def CalculateArea(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def CalculateArea(self):
        return 3.14 * self.radius * self.radius
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def CalculateArea(self):

        return self.length * self.width
    
cir = circle(5)

print("Area of circle")
print(cir.CalculateArea())

rect= Rectangle(4,5)

print("Area of Rectangle")
print(rect.CalculateArea())