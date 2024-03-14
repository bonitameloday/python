
from abc import *

class Vehicle(metaclass = ABCMeta):
    
    @abstractmethod
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def move(self):
        pass

    def info(self):
        pass

    def honkhorn(self):
        pass

class  Car(Vehicle):
    
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
        
    def move(self):
        return print('60킬로 이동합니다.')

    def info(self):
        return print('자동차 색상: {}, 바퀴 수: {}'.format(self.color, self.wheels))

    def honkhorn(self):
        return print('빵빵아악~~')

class  Bicycle(Vehicle):
    
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
        
    def move(self):
        return print('30킬로 이동합니다.')

    def info(self):
        return print('자동차 색상: {}, 바퀴 수: {}'.format(self.color, self.wheels))

    def honkhorn(self):
        return print('따르릉따릉~~')

mycar = Car('노랑', 4);
mycar.info();
mycar.move();
mycar.honkhorn();

mybic = Bicycle('파랑', 2);
mybic.info();
mybic.move();
mybic.honkhorn();


