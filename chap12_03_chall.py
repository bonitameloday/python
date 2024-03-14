
class Car:

    def __init__(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color

    def __str__(self):
        return '자동차 회사: {}, 년식: {}, 색상: {}'.format(self.company, self.year, self.color)

    def __eq__(self, other):
        if self.company == other.company:
            return True
        else:
            return False

mycar = Car('현대', 2020, '검정')
yourcar = Car('기아', 2021, '백색')
print(mycar)
print(yourcar)
print(mycar == yourcar)



