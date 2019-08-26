def deco(func):  
    print("before myfunc() called.")  
    func()  
    print("  after myfunc() called.")  
    return func  
  
def myfunc():  
    print(" myfunc() called.")  
  
myfunc = deco(myfunc)  
#------------------------------------------------------------------
myfunc()  
myfunc()
print("------------------------------------------------------------------")

def deco2(arg):
    print("test1")
    print(arg)
    def _deco2(func):
        print("fun2Test")
        print(func)
        def __deco2():  
            print("before %s called [%s]." % (func.__name__, arg))  
            func()  
            print("  after %s called [%s]." % (func.__name__, arg))  
        return __deco2  
    return _deco2 

print("test2")
@deco2("mymodule")  
def myfuncc():  
    print(" myfunc() called.")  
 
@deco2("module2")  
def myfuncc2():  
    print(" myfunc2() called.")  

print("------------------------------------------------------------------")

myfuncc()
print("------------------------------------------------------------------")
myfuncc2()
