
class Student:

    def __init__(self, univ, name):
        self.univ = univ
        self.name = name
        
    def info(self):
        print('대학: ' + self.univ + ' 이름: ' + self.name)

i = Student('한국대학교', '이성실')
i.info()
