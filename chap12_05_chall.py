
class Circle:

    def __init__(self, radius):
      self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14

    def perimeter(self):
        return self.radius * 3.14 * 2

class Cylinder(Circle):

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return super().area() * 2 + super().perimeter() * self.height

    def volume(self):
        return super().area() * self.height

cy = Cylinder(3, 5)
print('원통 체적: %.2f' % cy.volume())
print('원톧 표면적: %.2f' % cy.area())
