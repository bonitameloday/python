
from abc import *

class Polygon(metaclass = ABCMeta):
    @abstractmethod
    def area(self): # 추상 메소드
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): # 부모 클래스의 추상 메소드 구현
        return self.width * self.height

rect = Rectangle(2, 4)
print('사각형 면적: %.2f' % rect.area())
        
