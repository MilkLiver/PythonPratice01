import time
import random

def timer(fun):
    def timerstart():
        start=time.time()
        fun()
        end=time.time()
        return "used time: {:.5f}s".format((end-start))
    return timerstart

@timer
def foo():
    print('in foo()')
 
print(foo())

print("-----------------------------------------------------------------------")
