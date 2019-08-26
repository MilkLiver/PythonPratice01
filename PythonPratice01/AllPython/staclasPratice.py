def foo(x):
    print ("executing foo(%s)"%(x))

class A(object):
    a="test"
    def __init__(self,t):
        self.t=t
        
    def foo(self,x):
        print ("executing foo(%s,%s)"%(self,x))
        print(a)

    @classmethod
    def class_foo(cls,x):
        print ("executing class_foo(%s,%s)"%(cls,x))
        print(a)
        
    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)
        print(a)

a=A(5)
a.foo("OwO")
a.class_foo("OwO")
a.static_foo("OwO")
print('')
A.foo("","OAO")
A.class_foo("OAO")
A.static_foo("OAO")
