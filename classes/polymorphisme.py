# polimorfisme adalah sambungan / interface dari class, digunakan untuk membuat code lebih bersih

# 1. polimorfisme method
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

# Penggunaan
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow

# polimorfisme inheritence
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

def print_area(shape):
    print("Area:", shape.area())

# Penggunaan
rectangle = Rectangle(10, 5)
circle = Circle(7)

print_area(rectangle)  # Output: Area: 50
print_area(circle)     # Output: Area: 153.86

