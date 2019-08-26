def foo(x):
    return x

a=foo(3)
print(a)
print(callable(foo))
print(callable(a))

def foo2(x):
    def test():
        pass
    return test

print("--------------------------------------------------------------------------------")

a2=foo2(3)
print(a2)
print(callable(foo2))
print(callable(a2))

print("--------------------------------------------------------------------------------")

class Test:
    a=1
    b=2
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __call__(self,c):
        print(self.a*c,self.b*c)
        
t1=Test(4,5)
print(callable(Test))
print(callable(t1))
t1(4)
