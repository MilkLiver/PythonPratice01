class Some:
    a=15

    def __init__(self,a):
        self.a=a
    
    @staticmethod
    def service(x, y):
        print('statictest')

    def fun1(self,x):
        print('funtest')

    @classmethod
    def fun2(cls,x):
        print('classtest')

Some(5).fun1(5)
Some.fun1(Some,5)
Some.service(1,2)
Some(3).service(1,2)
Some(3).fun2(1)
Some.fun2(1)
print(isinstance(Some(5),Some))
a=Some(1)
b=Some(2)
print(a.__class__ is b.__class__)

class A():
    def test(self):
        print('testA')

class B(A):
    def test(self):
        super().test()
        print('testB')

class C(A):
    def test(self):
        print('testC')

class D(B,C):
    def test(self):
        super().test()
        print('testD')
        
D().test()
