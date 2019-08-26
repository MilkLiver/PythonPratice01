import math
class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius
    
    @property
    def radius(self):
        print("Pradius")
        return self.__radius

    '''@radius.getter
    def radius(self):
        print("getter test")
        return self.__radius'''
    
    @property
    def volumn(self):
        print("Pvolumn")
        return 4.0 / 3.0 * math.pi * self.__radius ** 3
    
    @volumn.setter
    def volumn(self, volumn):
        print("PvolumnSetter")
        if volumn <= 0:
            raise ValueError('必須是正數')
        self.__radius = ((3.0 * volumn) / (4.0 * math.pi)) ** (1.0 / 3.0)
        
ball = Ball(10.0)
print("----------------------------------------------------------------------")
print(ball.volumn)
print("----------------------------------------------------------------------")
ball.volumn = 5000
print("----------------------------------------------------------------------")
print(ball.radius)
print("----------------------------------------------------------------------")
print(ball.__dict__)
print(ball._Ball__radius)
ball.radius
