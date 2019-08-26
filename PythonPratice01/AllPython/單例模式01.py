from functools import wraps
class Singleton(object):
    __instance = None
    def __new__(cls, *args, **kwargs):  # 這裡不能使用__init__，因為__init__是在instance已經生成以後才去調用的
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
print(s1.__class__.__class__)
print(object.__class__)
print(type.__mro__)
#print(type.__dict__)
print(isinstance(type,object))
print('----------------------------------------------------------------------')

class  Singleton2 (object) :
    _instance = None
    def  __new__ (cls, *args, **kw) :
        if cls._instance is None:
            #cls._instance = super(Singleton2, cls).__new__(cls, *args, **kw)
            cls._instance = object.__new__(cls, *args, **kw)
            print("class:",Singleton2.__class__,"base:",Singleton2.__base__)
            #print(cls.mro())
            #print(cls)
            #cls._instance=super().__new__(cls, *args, **kw)
            #cls._instance=type(cls, *args, **kw)
            #cls._instance=type.__new__(type,cls, *args, **kw)
            print('cls:',cls._instance,'class:',cls.__class__,'name:',cls.__name__)
        return cls._instance
    
class  MyClass (Singleton2) :  
    a = 1
    
one = MyClass()
two = MyClass()

print(one == two)
print(one is two)
print(id(one), id(two))
print(type(one),type(two))
print(hasattr(type,'__new__'))
print('----------------------------------------------------------------------')

def Singleton3(cls):
    instance_={}
    print("cls:",cls.__name__,cls.__class__)
    print("instance_:",instance_)
    @wraps(cls)
    def CreateInstance_(*args,**kwargs):
        if instance_=={}:
            instance_[cls]=cls(*args,**kwargs)
        return instance_[cls]
    return CreateInstance_

@Singleton3
class test1():
    pass

print("t1")
t1=test1()
print("t2")
t2=test1()
print(id(t1), id(t2))
print("t1:",t1.__class__,type(t1))
#print(help(type))
print('----------------------------------------------------------------------')

class Singleton(type):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: # 記得要透過 cls 來存取__instance 這個 class attribute 喔
            cls.__instance = super().__new__(cls, *args, **kwargs)  # 即使用了 super()還是得加 cls?!
        return cls.__instance

class Hello(metaclass=Singleton): pass

print(id(Hello()))  # 兩次實體化 id 不同！失敗了！
print(id(Hello()))



