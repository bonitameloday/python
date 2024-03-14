
class Student:
    
    def __init__(self, name, dept, mid, final):
        
        self.name = name
        self.dept = dept
        self.mid = mid
        self.final = final
        
        
    def __str__(self):
        
        return '학과: {}, 이름: {}, 중간: {}, 기말: {}'.format(self.dept, self.name, self.mid, self.final)

    def grade(self, mid, final):
        
        if(self.mid + self.final) / 2 >= 90:
            return print('학점: A')
        
        elif(self.mid + self.final) / 2 >= 80:
            return print('학점: B')
        
        elif(self.mid + self.final) / 2 >= 70:
            return print('학점: C')
        
        elif(self.mid + self.final) / 2 >= 60:
            return print('학점: D')
        
        elif(self.mid + self.final) / 2 < 60:
            return print('학점: F')
        

i = Student('김경철', ' 기계학과', 89, 90)
print(i)
i.grade(89, 90)
            
            
