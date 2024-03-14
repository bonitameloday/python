class Rectangle:
    '''사각형을 표현하는 클래스 정의'''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rec = Rectangle(2.1, 3.4)
print(rec.area())
        

