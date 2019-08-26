import time

def dtest(fun):
    print("test")
    print(fun)


@dtest
def fun1(a):
    return a

#-------------------------------------------------------------
print("-------------------------------------------------------")

def logged(func):
    print("OwO")
    def with_logging(a): 
        print(func.__name__ + " was called" )
        print(a)
        return func(a) 
    return with_logging

def logged2(func):
    print("OwO")
    def with_logging(a):
        print(func.__name__ + " was called" )
        print("this is decorator test")
        print("a=",a)
        #a=7
        return func(a)
    return with_logging

print("OHO")
@logged2 
def f(x): 
   """does some math"""
   print("test")
   return x + x * x

print("OAO")
print(f(3))

#-------------------------------------------------------------
print("-------------------------------------------------------")

def f2(x): 
   """does some math"""
   print("test")
   return x + x * x

print(logged2(f2)(5))
