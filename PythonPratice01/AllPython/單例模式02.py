from functools import wraps

def Singleton3(cls):
    instance_=None
    print("cls:",cls.__name__,cls.__class__)
    print("instance_:",instance_)
    @wraps(cls)
    def CreateInstance_(*args,**kwargs):
        nonlocal instance_
        if instance_==None:
            instance_=cls(*args,**kwargs)
        return instance_
    return CreateInstance_

@Singleton3
class test1():
    pass

#print(test1.__doc__)
print("t1")
t1=test1()
print("t2")
t2=test1()
print(id(t1), id(t2))
print(type(t1))
print(id(test1))
print(id(test1()))

print("----------------------------------------------------------------------")

class Singleton(type):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

class Hello(metaclass=Singleton): pass

print(id(Hello())) 
print(id(Hello()))
