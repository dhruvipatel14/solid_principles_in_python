# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * (shape.radius ** 2)

    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2 * (shape.width + shape.height)
        elif shape.type == "circle":
            return 2 * 3.14 * shape.radius


# Need to add the new shape, Above class violates Open/close principle
# We can create a new Abstract class and each shape can inherit that and can use existing methods and add new methods


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Triangle(Shape):
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
