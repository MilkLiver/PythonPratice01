import random

class test:
    a=10
    b=20
    def __init__(self):
        self.a=random.randint(1,10)
        #print(self.b,id(self.b))
        self.b=random.randint(10,20)

t1=test()
t2=test()
print(t1.a,id(t1.a))
print(t2.a,id(t2.a))
print(t1.b,id(t1.b))
print(t2.b,id(t2.b))

print("------------------------------------------------------------------------")

class Some:
    a=15

    def __init__(self,a):
        self.a=a
    
    @staticmethod
    def service(x, y):
        print('do service...', x + y)

    def fun1(self,x):
        print(self.a,x)

    @classmethod
    def fun2(cls,x):
        print(cls.a,x)


Some.service(10, 20) 

s = Some(11)
s.service(10, 20)
print(s.a)

print("------------------------------OwO------------------------------------------")

s.fun1(5)
#Some.fun1(5) #error
Some.fun1(s,5)

print("------------------------------------------------------------------------")

s.fun2(5)
Some.fun2(5)
#Some.fun2(s,5) #error

print("------------------------------OAO------------------------------------------")
s.a=87
s.fun2(5)
print(s.a)

