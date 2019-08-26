def Foo(cls):
    def ftest():
        print("ftest")
        return cls()
    return ftest

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ )     # 输出 'with_logging'
        print(func.__doc__ )      # 输出 None
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x

f(5)
logged(f(5))
