def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)	# 以类名作为实例化的标准,每个类名只能被实例化一次
            #print("cls:",instances[cls])
        return instances[cls]  
    return _singleton

@singleton
class MyClass(object):
    def __init__(self, x=0):
        self.x = x  

cl1=MyClass()
cl2=MyClass()
print("cl1 id:"+str(id(cl1)))
print("cl2 id:"+str(id(cl2)))
print(cl1.__class__)
        
