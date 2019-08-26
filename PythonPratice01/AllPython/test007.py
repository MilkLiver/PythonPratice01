fib = lambda n: n if n < 2 else 2 * fib(n - 1)
print(fib(4))
print(fib(5))
print(fib(6))

print("------------------------------------------------------------------")
class test:
    a=10
    b=20
    c=30
    '''def __init__(self):
        self.c=40'''
    def reset(self):
        self.a=11
        self.b=22
    def print(self):
        print(self.a,self.b,self.c)


t1=test()
print(t1.a,id(t1.a))
print(test.a,id(test.a))
t1.a=40
print(t1.a,id(t1.a))
print(test.a,id(test.a))
t1.reset()
print(t1.a,id(t1.a))
print(test.a,id(test.a))

print("------------------------------------------------------------------")
print(test.c,id(test.c))
print(t1.c,id(t1.c))
test.c=80
print(test.c,id(test.c))
print(t1.c,id(t1.c))
t1.c=87
print(test.c,id(test.c))
print(t1.c,id(t1.c))

print("------------------------------------------------------------------")

class test2:
    a=10
    b=20
    c=30
    d=40
    def __new__(cls):
        return test


t2=test2()
print(test.c,id(test.c))
print(t2.c,id(t2.c))
test.c=90
print(test.c,id(test.c))
print(t2.c,id(t2.c))
print(test.a,id(test.a))
print(t2.a,id(t2.a))
print(t1.a,id(t1.a))

print("------------------------------------------------------------------")

class test3:
    a=10
    b=20
    c=30
    d=40
    def __init__(self):
        self.a=11
        self.b=21

tt1=test3()
tt2=test3()
print(tt1.a,id(tt1.a))
print(tt2.a,id(tt2.a))
print(test3.a,id(test3.a))
test3.a=87
print(tt1.a,id(tt1.a))
print(tt2.a,id(tt2.a))
print(test3.a,id(test3.a))
tt1.a=687
print(tt1.a,id(tt1.a))
print(tt2.a,id(tt2.a))
print(test3.a,id(test3.a))

